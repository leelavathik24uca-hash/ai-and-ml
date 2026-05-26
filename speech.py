# Simple Speech Recognition AI Program
# Install required libraries first:
# pip install SpeechRecognition pyaudio

import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

# Use microphone as input
with sr.Microphone() as source:
    print("Speak something...")

    # Reduce noise
    recognizer.adjust_for_ambient_noise(source)

    # Listen to audio
    audio = recognizer.listen(source)

try:
    # Convert speech to text using Google Speech API
    text = recognizer.recognize_google(audio)

    print("\nYou said:", text)

except sr.UnknownValueError:
    print("Sorry, could not understand audio")

except sr.RequestError:
    print("Internet connection error")