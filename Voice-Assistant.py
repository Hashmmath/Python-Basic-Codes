'''This code initializes a SpeechRecognition recognizer and a 
pyttsx3 text-to-speech engine. The speak function takes a text 
argument and speaks it using the engine. The listen function 
uses the recognizer to listen for speech, recognizes it using 
Google's speech recognition service, and returns the 
recognized text. The main loop listens for speech, interprets 
it using some basic conditional statements, and responds using 
the speak function. You can add more conditional statements to 
respond to other commands or questions as needed.'''

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand what you said.")
        except sr.RequestError:
            speak("Sorry, I couldn't connect to the speech recognition service.")

# Main loop for the voice assistant
while True:
    # Listen for speech
    text = listen()

    # Interpret the speech and respond
    if text:
        if "hello" in text.lower():
            speak("Hello! How can I help you?")
        elif "what's the time" in text.lower():
            # Add code here to get the current time
            speak("The time is 12:34 PM.")
        elif "goodbye" in text.lower():
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't know how to respond to that.")
