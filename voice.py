import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio)
        return command.lower()

while True:
    command = listen()
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        import webbrowser
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "exit" in command:
        speak("Goodbye!")
        break