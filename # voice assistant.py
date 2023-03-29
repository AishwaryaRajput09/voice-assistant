# voice assistant
import pyttsx3 #pip install pyttsx3 
import speech_recognition as sr # Setting up the function for listening
import datetime  # imported for getting date and time
import wikipedia  # pip install wikipedia
import webbrowser  # Setting up the function for opening browser
import os  # for interacting with opertaing system
import smtplib  # Setting up the function for sending email

engine = pyttsx3.init('sapi5')  # sapi5 is the voice engine
voices = engine.getProperty('voices') # getting details of current voice
engine.setProperty('voice', voices[1].id)  # set the voice
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 160) # changing speaking rate of voice
def speak(audio):  # Function for speaking the audio
    engine.say(audio) 
    engine.runAndWait() 

def wishMe():  # Function for greeting
    hour = int(datetime.datetime.now().hour)  # Getting the current hour
    if hour >= 0 and hour <= 12: # Checking if the hour is between 0 and 12
        speak("Good Morning Sir")
    elif hour>= 12 and hour <18: # Checking if the hour is between 12 and 18
        speak("Good Afternoon Sir")
    else:                      # Checking if the hour is between 18 and 24
        speak("Good Evening Sir")
    speak("I am your Virtual Assistant. Please tell me how may I help you")

def TakeCommand():  # Function for taking command
    r = sr.Recognizer()  # Setting up the function for listening
    with sr.Microphone() as source:  
        print("Listening...") # Printing the message
        r.pause_threshold = 1  
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognizing the audio
        print(f"User said: {query}\n")  # Printing the message
    except Exception as e:  # Checking if the audio is not recognized 
        print("Say that again please...")  # Printing the message
        return "None"  # Returning none
    return query  # Returning the query

# wishMe() # Calling the function for greeting
if __name__== "__main__":  # Checking if the file is being run as main file
    wishMe()  # Calling the function for greeting
    while True:
        query = TakeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stackoverflow")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening Facebook")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Opening Gmail")

        elif 'open Linkedin' in query:
            webbrowser.open("linkedin.com")
            speak("Opening Linkedin")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("Opening Instagram")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
            speak("Opening Twitter")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            speak("Opening Whatsapp")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            speak("Opening Amazon")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'news' in query:
            news = webbrowser.open("https://news.google.com/news/rss")
            speak("Here are some news")

        elif 'search' in query:
            speak("What do you want to search for?")
            search = TakeCommand()
            url = "https://google.com/search?q=" + search
            webbrowser.open(url)
            speak("Here are some results")

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Mukesh and Aishwarya")

        elif 'good bye' in query or 'bye' in query or 'exit' in query or 'quit' in query:
            speak("Bye Sir, have a good day.")
            break
    