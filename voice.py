# Simple AI Voice Assistant in Python

# Install these first:
# pip install speechrecognition pyttsx3 pyaudio

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I did not understand.")
        return ""

# Welcome message
speak("Hello! I am your AI voice assistant.")

# Main loop
while True:
    command = listen()

    # Time
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)

    # Date
    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    # Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Exit
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    # Unknown command
    elif command != "":
        speak("Command not recognized.")