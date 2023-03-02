<div id="top"></div>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/idosh333/chatgptdirect">
    <img src="https://imgur.com/zTylAmd.png" alt="Logo" width="500" height="500">
  </a>

<h3 align="center">ChatGPT Direct</h3>

  <p align="center">
    An easy-to-use chatGPT mimic using OpenAI's API.
    <br />
    <a href="https://github.com/idosh333/chatgptdirect"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/idosh333/chatgptdirect#product-example">View Demo</a>
    ·
    <a href="https://github.com/idosh333/chatgptdirect/issues">Report Bug</a>
    ·
    <a href="https://github.com/idosh333/chatgptdirect/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

ChatGPTDirect was created to bypass queues when using `chat.openai.com/chat`.
By using the chatGPT API directly and OpenAI's Python library,
this project became possible. This project was initially made for personal use,
so please use at your own risk.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

[![Python][made-with-python]][python-url]

<!-- GETTING STARTED -->

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

<!-- PREREQUISITES -->

### Prerequisites
To run this project, you'll need to have the Python installed(3.8 or higher).

<!-- INSTALLATION -->
### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/idosh333/chatgptdirect.git
   ```
2. Install the required python packages either by running `install_requirements.bat`,
   or by running the next command in the directory of the folder:
   ```sh
   pip install -r requirements.txt
   ```
3. Get your OpenAI API key from [OpenAI's API dashboard][openai-api-key].
4. Create a new `.env` file and add your OpenAI API key like so:
   ```
   API_KEY=YOUR_API_KEY_HERE
   ```

<!-- USAGE-->

### Usage

1. Run the project either by using `run.bat` file or open a by running
   the next command:
   ```
   streamlit run chatgpt.py
   ```
2. A new browser tab should open automatically with the application running.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- FYI -->

### Nice to know

1. You can submit your prompt using Ctrl+Enter or the Submit button.
2. You can delete the chat history using the Clear Chat History button.
3. The project is dynamic and can be run on any screen size.
4. Since the project is built with Streamlit, it can be viewed in both light and dark modes.
   Click on the hamburger icon on the right of the screen to change Streamlit's settings.
5. The project was built in less than a day. 😉

<!-- EXAMPLES -->

### Product example

<img src="https://i.imgur.com/yW47MiO.png" alt="example of use" width="1400" height="">

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Ido Shayovitz - ido.sh333@gmail.com

Project Link: [https://github.com/idosh333/chatgptdirect](https://github.com/idosh333/chatgptdirect)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/idosh333/chatgptdirect.svg?style=for-the-badge
[contributors-url]: https://github.com/idosh333/chatgptdirect/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/idosh333/chatgptdirect.svg?style=for-the-badge
[forks-url]: https://github.com/idosh333/chatgptdirect/network/members
[stars-shield]: https://img.shields.io/github/stars/idosh333/chatgptdirect.svg?style=for-the-badge
[stars-url]: https://github.com/idosh333/chatgptdirect/stargazers
[issues-shield]: https://img.shields.io/github/issues/idosh333/chatgptdirect.svg?style=for-the-badge
[issues-url]: https://github.com/idosh333/chatgptdirect/issues
[license-shield]: https://img.shields.io/github/license/idosh333/chatgptdirect.svg?style=for-the-badge
[license-url]: https://github.com/idosh333/chatgptdirect/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ido-shayovitz
[product-screenshot]: images/screenshot.png
[made-with-python]: http://ForTheBadge.com/images/badges/made-with-python.svg
[python-url]: https://www.python.org/downloads/release/python-3112/
[openai-api-key]: https://platform.openai.com/account/api-keys
