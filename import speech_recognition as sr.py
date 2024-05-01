import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None

    return query.lower()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you today?")

# Function to execute voice commands
def execute_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'time' in command:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {str_time}")
    elif 'bye' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# Main program loop
if __name__ == "__main__":
    greet()

    while True:
        command = listen()

        if command:
            execute_command(command)
