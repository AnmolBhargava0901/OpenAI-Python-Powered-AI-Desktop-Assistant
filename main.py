import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from openai import OpenAI
from config import apikey
import time

chatStr = ""

# Initialize OpenAI client once
client = OpenAI(api_key=apikey)

def say(text):
    """Speak the given text using pyttsx3"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listen from microphone and return recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(f"Error recognizing speech: {e}")
        say("Sorry, I didn't get that.")
        return ""

def ai(prompt):
    """Send prompt to OpenAI's chat completion and speak/save response"""
    global chatStr
    chatStr += f"User: {prompt}\nKira: "
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Kira, a helpful AI assistant."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response.choices[0].message.content.strip()
        chatStr += answer + "\n"
        say(answer)

        # Save conversation
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        filename = f"Openai/{int(datetime.datetime.now().timestamp())}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Prompt:\n{prompt}\n\nResponse:\n{answer}\n")

    except Exception as e:
        say("Sorry, there was a problem with artificial intelligence.")
        print(f"OpenAI error: {e}")

def greet_user():
    """Greet user based on time"""
    hour = int(datetime.datetime.now().strftime("%H"))
    if 5 <= hour < 12:
        say("Good morning!")
    elif 12 <= hour < 17:
        say("Good afternoon!")
    elif 17 <= hour < 21:
        say("Good evening!")
    else:
        say("Hello!")
    say("I am Kira. How can I help you?")

if __name__ == '__main__':
    print('Welcome to Kira A.I')
    greet_user()

    WAKE_WORD = " hey Kira"

    special_sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "brave": "https://brave.com/",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://twitter.com",
        "reddit": "https://www.reddit.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com",
        "whatsapp web": "https://web.whatsapp.com",
        "netflix": "https://www.netflix.com",
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
        "myntra": "https://www.myntra.com",
        # Add more sites as needed
    }

    while True:
        print("Waiting for wake word...")
        query = takeCommand().lower().strip()

        if WAKE_WORD in query:
            say("Yes, sir?")
            query = takeCommand().lower().strip()
            if not query:
                say("Please say that again.")
                continue

            # Check if command is to open website/app
            if "open" in query:
                found = False
                for site in special_sites:
                    if site in query:
                        say(f"Opening {site.capitalize()}")
                        webbrowser.open(special_sites[site])
                        found = True
                        break
                if not found:
                    # Try generic www.sitename.com url
                    site = query.replace("open", "").strip().replace(" ", "")
                    url = f"https://www.{site}.com"
                    say(f"Opening {site.capitalize()}")
                    webbrowser.open(url)

            elif "the time" in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                say(f"Sir, the time is {current_time}")

            elif "exit" in query or "Kira quit" in query:
                say("Goodbye, sir!")
                break

            else:
                # For any other query, use AI to search & answer
                say("Let me check on that...")
                ai(query)

        else:
            # If wake word not detected, wait a moment before listening again
            time.sleep(1)
