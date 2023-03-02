import html
import streamlit as st
import openai
import os
import keyboard

from datetime import datetime
from dotenv import load_dotenv


# Get api key from .env file
load_dotenv()
openai.api_key = os.environ.get('API_KEY')

model_engine = "text-davinci-003"  # set the default language model

st.set_page_config(page_title="GPT Direct",
                   page_icon=":speech_balloon:", layout="wide")


def generate_response(prompt, model_engine, temperature=0.5, max_tokens=1024):
    with st.spinner(text="Thinking..."):
        prompt_history = get_prompt_history()
        full_prompt = (prompt_history + ' answer this: ' + prompt).strip()
        response = openai.Completion.create(
            engine=model_engine,
            prompt=full_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=None,
        )
        message = response.choices[0].text.strip()
        add_to_chat_history(prompt, message)


def get_prompt_history():
    if len(st.session_state.chat_history) < 1:
        return ""
    history = ""
    for tup in st.session_state.chat_history:
        history += f'My prompt was: {tup[0].strip()}. Your response was: {tup[1].strip()}.'
    return history.strip()


def add_to_chat_history(prompt, response):
    time = datetime.now().strftime("%H:%M:%S")
    st.session_state.chat_history.append((prompt, response, time))


def display_chat():
    # Display the chat history
    for chat_entry in st.session_state.chat_history:

        prompt = html.escape(chat_entry[0])
        response = html.escape(chat_entry[1])
        time = html.escape(chat_entry[2])

        st.write(
            f'<div class="message"><b>Prompt:</b> {prompt}<span style="float: right">{time}</span></div>', unsafe_allow_html=True)
        st.write(
            f'<div class="message"><b>Response:</b> {response}<span style="float: right">{time}</span></div>', unsafe_allow_html=True)


def on_prompt_change(prompt):
    if len(prompt) > 3 and "Control" in prompt and "Enter" in prompt:
        generate_response(prompt, model_engine)


def main():
    st.title("Chat with GPT API Directly")

    # Initialize the session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

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

    # Create the input prompt field and send button
    input_container = st.container()
    send_button = st.button("Send", key="send_button")
    reset_button = st.button("Clear Chat History", key="clear_button")

    with input_container:
        prompt = st.text_area("Type your prompt here",
                              key="prompt", height=50, max_chars=20000)

    if len(prompt) > 3:
        if send_button:
            generate_response(prompt, model_engine)

        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("enter"):
            generate_response(prompt, model_engine)

    if reset_button:
        st.session_state.chat_history = []

    display_chat()


if __name__ == "__main__":
    main()
