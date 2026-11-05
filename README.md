# Translate Go

A desktop app that translates text between languages. Type your text or speak it, pick a language, and get the translation. Built with Python.


## Features

- **Type or speak:** choose text input, or use voice input from your microphone.
- **Language selection:** pick the target language from a dropdown menu.
- **Clear errors:** the app shows a message if your speech isn't recognized or a translation fails, instead of crashing.

## Built with

- Python 3
- customtkinter (the window and buttons)
- SpeechRecognition (voice input, uses Google's speech service)
- googletrans (translation)

## Run it

1. Install Python 3.
2. Clone the repo and open the folder:

```
git clone https://github.com/zinoiu/Python-Project.git
cd Python-Project
```

3. Install the libraries:

```
pip install customtkinter SpeechRecognition googletrans PyAudio
```

4. Start the app:

```
python Main.py
```

Voice input needs a microphone and an internet connection. If PyAudio won't install, you can still use text input. If googletrans gives errors, try `pip install googletrans==4.0.0rc1`.
