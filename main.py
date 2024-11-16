import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyaudio
import setuptools
import webbrowser
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def openWebsite(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.co.in/")
        speak(f"opening google..")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com/")
        speak(f"opening instagram..")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
        speak(f"opening youtube..")
    elif "open facebook" in command.lower():
        webbrowser.open("https://web.facebook.com/")
        speak(f"opening facebook..")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com//")
        speak(f"opening linkedin..")

def play_on_yt(command):
    if "play" in command.lower():
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        speak(f"playing {song}")

def search_on_web(command):
    words = ["what", "how", "when", "where", "who", "whom", "why"]
    if any(word in command.lower() for word in words):
        search_query = command.lower()
        webSearch = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(webSearch)
        speak(f"searching for {search_query}")

def open_application(command):
    applications = {"notepad" : "notepad.exe",
                    "calculator" : "calc.exe",                    
                    "file explorer" : "explorer.exe"
                    }
    for app in applications:
        if app in command.lower():
            try:
                os.system(applications[app])
                speak(f"opening {app}")
            except Exception as e:
                print(f"sorry {app} has denied permission to open")
                break

if __name__ == "__main__":
    speak("Initializing hanuman...")
    while True:
        r = sr.Recognizer()
        print("Listening...")

        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=3, phrase_time_limit=10)
                print("recognizing...")
                word = r.recognize_google(audio)
                if word.lower() == "hanuman":
                    print("Hanuman is now active...")
                    speak("yeah, how can i help you?")
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        print("listening...")
                        command = r.recognize_google(audio)

                        openWebsite(command)
                        play_on_yt(command)
                        search_on_web(command)
                        open_application(command)

        except Exception as e:
            print(f"google speech recognition cannot understand {e}")