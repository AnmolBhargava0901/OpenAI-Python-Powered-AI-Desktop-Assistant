# Jarvis A.I - Voice Activated Assistant

**Jarvis A.I** is a Python-based voice assistant that can recognize speech, speak responses, open websites, answer queries using OpenAI's GPT model, and respond based on time and context.

---

## Features

* Wake word activated ("Jarvis")
* Opens popular websites like YouTube, Google, Facebook, etc.
* Answers general queries using OpenAI's GPT-3.5 Turbo
* Speaks responses using `pyttsx3`
* Saves AI conversations to timestamped `.txt` files
* Tells the current time

---

## Requirements

### Python Version

* Python 3.7+

### Python Packages

Install the dependencies using pip:

```bash
pip install speechrecognition pyttsx3 openai
```

Additional packages:

* `pyaudio` (for microphone input) — may require special installation steps depending on OS.
* `webbrowser` (comes built-in with Python)

For Windows users having trouble with `pyaudio`, install via wheel:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Project Structure

```
JarvisAI/
├── jarvis.py           # Main Python script (your code)
├── config.py           # Stores OpenAI API key (add manually)
├── Openai/             # Stores AI chat logs with timestamps
└── README.md           # This file
```

---

## Setup

### 1. Add Your API Key

Create a file named `config.py` and add:

```python
apikey = "your-openai-api-key"
```

### 2. Run the Project

In terminal or command prompt:

```bash
python jarvis.py
```

### 3. Speak to Jarvis

Use the wake word "Jarvis" followed by your command.

Examples:

* "Jarvis, open YouTube"
* "Jarvis, what's the time?"
* "Jarvis, who is Elon Musk?"

---

## Customization

* **Add More Sites**: Update the `special_sites` dictionary.
* **Change Wake Word**: Modify the `WAKE_WORD` variable.
* **Improve AI Memory**: Extend or persist `chatStr`.

---

## Troubleshooting

* If microphone doesn't work, check audio permissions or device index.
* If OpenAI doesn't respond, check internet and API key.

---

## License

This is an educational project. You are free to modify and distribute it.

