# Text-2-Speech Application using Python and pyttsx3

## Introduction

This is the version 2.0 of a simple Text-to-Speech (TTS) application developed by me using Python and the pyttsx3 library. The application allows users to convert text into speech, enabling them to listen to the content rather than reading it. It can be useful for various applications, such as creating audiobooks, assisting individuals with visual impairments, or enhancing accessibility in applications. The modification and improvement I did over the version 1.0 are some basic UI improvements as well as the addition of the feature to allow to download or save the audio file.

## Requirements

- Python 3.x
- pyttsx3 library

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/text-to-speech-app.git
```

2. Change the directory to the project folder:

```bash
cd text-to-speech-app
```

3. Install the required dependencies using pip:

```bash
pip install pyttsx3
```

## Usage

1. Run the Python script to start the Text-to-Speech application:

```bash
python text_to_speech.py
```

2. The application will prompt you to enter the text you want to convert to speech. Type the text and press Enter.

3. The application will then utilize the pyttsx3 library to convert the text into speech and play it back through your default audio output device.

## Customization

You can further customize the application as per your needs. For example:

- Modify the voice settings such as voice type, pitch, and rate.
- Implement a GUI for a more user-friendly interface using libraries like tkinter or PyQT.
- Save the generated speech as an audio file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of [pyttsx3](https://pypi.org/project/pyttsx3/) for providing the text-to-speech library for Python.
- Inspiration and guidance from various online tutorials and resources.

Happy Text-to-Speech-ing!
