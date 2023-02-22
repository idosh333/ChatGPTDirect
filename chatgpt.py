import streamlit as st
import openai
import os

from datetime import datetime
from dotenv import load_dotenv


# Initialize the session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Get api key from .env file

load_dotenv()

openai.api_key = os.environ.get('API_KEY')
model_engine = "text-davinci-003"  # set the default language model

st.set_page_config(page_title="GPT Direct",
                   page_icon=":speech_balloon:", layout="wide")


def generate_response(prompt, model_engine, temperature=0.5, max_tokens=60):
    if "session_chat_history" not in st.session_state:
        st.session_state.session_chat_history = []
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    message = response.choices[0].text.strip()
    time = datetime.now().strftime("%H:%M:%S")
    st.session_state.session_chat_history.append((prompt, message, time))
    return message


def add_to_chat_history(prompt, response):
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    st.session_state.chat_history.append((time, prompt, response))


def chat_display(chat_history):
    # Display the chat history
    for chat_entry in chat_history:
        st.write(
            f'<div class="message"><b>Prompt:</b> {chat_entry[1]}<span style="float: right">{datetime.now().strftime("%H:%M:%S")}</span></div>', unsafe_allow_html=True)
        st.write(
            f'<div class="message"><b>Response:</b> {chat_entry[2]}<span style="float: right">{datetime.now().strftime("%H:%M:%S")}</span></div>', unsafe_allow_html=True)


def main():
    st.title("Chat with GPT API Directly")

    # Initialize the session state
    if "key_pressed" not in st.session_state:
        st.session_state.key_pressed = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Initialize the variables
    message = ""

    # Styling
    st.markdown(
        f"""
        <style>
          .message {{
            border: 1px solid gray;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
          }}
          .send {{
            display: flex;
            justify-content: flex-end;
            align-items: center;
          }}
        </style>
    """, unsafe_allow_html=True)

    # Create a selectbox to choose the language model
    model_engine = st.selectbox(
        "Choose a language model",
        ["text-davinci-003", "code-davinci-002",  "text-curie-001", "text-babbage-001",
         "text-ada-001", "code-cushman-001"],
        index=0,
        key='language_model',
        format_func=lambda x: x.upper()
    )

    # Create a column for the send button
    if st.session_state.key_pressed == "Enter":
        st.session_state.key_pressed = None
        st.text_input("", "", key="hidden")

    # Create the input prompt field and send button
    input_container = st.container()
    with input_container:
        prompt = st.text_input("Type your prompt here", key="prompt")
        st.write("")

    # Send the prompt when the send button is clicked
    send_button = st.button("Send", key="send_button")

    col1, col2 = st.columns([4, 1])
    if len(prompt) > 3:
        with st.spinner(text="Thinking..."):
            message = generate_response(prompt, model_engine)
            add_to_chat_history(prompt, message)
    else:
        col2.write(" ")

    if st.session_state.key_pressed is not None:
        js = ""
        if st.session_state.key_pressed == "Down":
            js = "window.scrollTo(0, document.body.scrollHeight);"
            html = f'< img src ="data: image/png'
            add_to_chat_history(prompt, message)
            
    chat_display(st.session_state.chat_history)

    # Listen for key events
    key_event = st.session_state.get("key_event")
    if key_event is not None:
        if key_event["type"] == "KEY_DOWN" and key_event["key"] == "Enter":
            st.session_state.key_pressed = "Enter"

        st.experimental_set_query_params(key_event=None)


if __name__ == "__main__":
    main()
