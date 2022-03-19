from email.mime import audio
from pip import main
import pyttsx3
from decouple import config
import datetime
import speech_recognition as sr
import random
import utils
import function.os_ops as os
import function.online_ops as on


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

        if "stop" not in query or "exit" not in query:
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
            ip=os.find_my_ip()
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")

        elif f"email to" in query: 
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