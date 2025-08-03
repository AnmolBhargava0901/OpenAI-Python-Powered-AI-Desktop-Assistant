# 🤖 Kira A.I - Voice Activated Assistant

**Kira A.I** is a Python-based voice assistant that can recognize speech, speak responses, open websites, answer queries using OpenAI's GPT model, and respond based on time and context.

---

## ✨ Features

* 🗣️ Wake word activated ("Kira")
* 🌐 Opens popular websites like YouTube, Google, Facebook, etc.
* 🧠 Answers general queries using OpenAI's GPT-3.5 Turbo
* 🔊 Speaks responses using `pyttsx3`
* 🗂️ Saves AI conversations to timestamped `.txt` files
* ⏰ Tells the current time

---

## ⚙️ Requirements

### 🐍 Python Version

* Python 3.7+

### 📦 Python Packages

Install the dependencies using pip:

```bash
pip install speechrecognition pyttsx3 openai
```

Additional packages:

* 🎙️ `pyaudio` (for microphone input) — may require special installation steps depending on OS.
* 🔗 `webbrowser` (comes built-in with Python)

For Windows users having trouble with `pyaudio`, install via wheel:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 📁 Project Structure

```
KiraAI/
├── Kira.py           # Main Python script (your code)
├── config.py           # Stores OpenAI API key (add manually)
├── Openai/             # Stores AI chat logs with timestamps
└── README.md           # This file
```

---

## 🚀 Setup

### 1️⃣ Add Your API Key

Create a file named `config.py` and add:

```python
apikey = "your-openai-api-key"
```

### 2️⃣ Run the Project

In terminal or command prompt:

```bash
python Kira.py
```

### 3️⃣ Speak to Kira

Use the wake word "Kira" followed by your command.

Examples:

* "Kira, open YouTube"
* "Kira, what's the time?"
* "Kira, who is Elon Musk?"

---

## 🛠️ Customization

* ➕ **Add More Sites**: Update the `special_sites` dictionary.
* 📝 **Change Wake Word**: Modify the `WAKE_WORD` variable.
* 🧠 **Improve AI Memory**: Extend or persist `chatStr`.

---

## 🧰 Troubleshooting

* ❌ If microphone doesn't work, check audio permissions or device index.
* 🌐 If OpenAI doesn't respond, check internet and API key.

---

## 📄 License

This is an educational project. You are free to modify and distribute it.

---


