from msilib.schema import AdvtUISequence
import pyttsx3
from decouple import config
import datetime
import speech_recognition as sr
import random
import utils
import function.os_ops as os
import function.online_ops as on
import requests


USERNAME=config("USER")
BOTNAME=config("BOTNAME")

emails = {
    "akash": "akashpatel1098@gmail.com",
    "patel": "patelakash1098@gmail.com",
    "sky": "onlyskymovie2020@gmail.com",
}

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

        if "stop" in query or "exit" in query:
             # greet before exiting
            if hour >=21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()    
        else:
           # greet before doing some task
            speak(random.choice(utils.opening_text))

    except Exception as e:
        # print(e)
        print("Sorry, I couldn't understand. Could you please say that again...")
        speak("Sorry, I couldn't understand. Could you please say that again?")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if "notepad" in query:
                os.open_notepad()

        elif "calculator" in query:
            os.open_calculator()

        elif "music" in query:
            os.playMusic()

        # elif "camera" in query:
        #     os.open_camera()#prblm
            
        elif "cmd" in query or "command prompt" in query:
            os.open_cmd()
        
        elif "wikipedia" in query: #prblm
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=on.search_on_wikipedia(query=query)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif "ip" in query:
            ip=on.find_my_ip()
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")

        elif "email to" in query: 
            '''these for loop initialise name with a key of dictionary emails if that key is in the query'''
            for key in emails.keys():
                if key in query:
                    to=key
                else:
                    pass
            try:
                speak("What should be the subject of email?")
                subject=takeCommand()
                speak("What should be the message,sir?")
                content=takeCommand()
                # to=[emails[name] for name in emails if name in query ]
                speak(f"Email is been sending to {emails[to]}")
                print(f"Email is been sending to {emails[to]}")
                speak("Please confirm this last time") 
                confirmation=takeCommand()
                if confirmation=="yes":
                    on.send_email(emails[to],subject,content)
                    speak("Email has been sent!")
                    print("Email has been sent!")
                else:
                    print("Please try again...")
                    speak("Please try again")
            except Exception as e:
                print(e)
                print("Sending email failed...")
                speak("Sorry,I am unable to send to the mail")

        # elif "open youtube" in query:
        #     speak("What should I play sir?")
        #     result=takeCommand().lower()
        #     on.search_on_youtube(result)

        # elif "open google" in query:
        #     speak("What should I search sir?")
        #     result=takeCommand().lower()
        #     on.search_on_google(result)
        elif "news" in query:
            speak("I'm reading out the latest news headlines, sir")
            result=on.get_latest_news()
            for title in result:
                speak(title)
                print(title)


        elif "joke" in query:
            speak("Hope you like this one sir")
            result=on.get_random_joke()
            print(result)
            speak(result)

        elif "advice" in query:
            speak("Here's an advice for you,sir")
            advice=on.get_random_advice()
            print(advice)
            speak(advice)

        elif "trending movie" in query:
            movies=on.get_trending_movies()
            print(f"Some of the trending movies are:")
            for movie in movies:
                print(movie)
            speak(f"Some of the trending movies are:{movies}")

        elif 'weather' in query:
            ip_address = on.find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            print(f"Getting weather report for your city {city}")
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = on.get_weather_report(city)
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")