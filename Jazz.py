from email.mime import audio
from pip import main
import pyttsx3
from decouple import config
import datetime
import speech_recognition as sr
import random
import utils


USERNAME=config("USER")
BOTNAME=config("BOTNAME")

engine=pyttsx3.init("sapi5")

# Set Rate
engine.setProperty("rate",190)
# Set Volume
engine.setProperty("volume",1.0)
# Set Voice
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

# Defining hour for getting the current hour 
hour=datetime.datetime.now().hour

def speak(audio):
    '''Used to speak by computer whatever text is passed'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function when run wish us in audio format according to time'''
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak(f"My name is {BOTNAME}. How may i help you")

def takeCommand():
    '''It listen the voice and convert and return it into string  '''
    #listen audio through microphone
    r=sr.Recognizer()
    with sr.Microphone() as source: #opening microphone
        print("\n\nListening...")
        r.pause_threshold=1
        audio=r.listen(source)#listen audio

    try:
        print("Recognizing...")
        #recognising audio  using google api and converting into string
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}")

        if not "stop" in query:
            # greet before doing some task
            speak(random.choice(utils.opening_text))
        else:
            # greet before exiting
            if hour >=21 and hour < 6:
                speak("Good night sir, take care!")
                exit()

            else:
                speak("Have a good day sir!")
                exit()

    except Exception as e:
        # print(e)
        print("Sorry, I couldn't understand. Could you please say that again...")
        speak("Sorry, I couldn't understand. Could you please say that again?")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    speak("Hello World")
    takeCommand()