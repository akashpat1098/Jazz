import pyttsx3
from decouple import config
import datetime
import speech_recognition as sr
import random
import json
import function.os_ops as os
import function.online_ops as on
import requests
import utils

# for naming the user and botname.It is just used when bot introduce herself
USERNAME=config("USER")
BOTNAME=config("BOTNAME")
# This is the phrases that Jazz uses before  doing some task
# defining the engine for Jazz to work
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
        # print anything that user says
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
    # loop for to continously listining by Jazz
    while True:
        # this is the entry point where Jazz listen its first command
        query=takeCommand().lower()
        # to open notepad 
        if "notepad" in query:
            os.open_notepad()
        # to open calculator
        elif "calculator" in query:
            os.open_calculator()
        # to play music
        elif "music" in query:
            os.playMusic()

        # elif "camera" in query:
        #     os.open_camera()#prblm

        # to open command prompt 
        elif "cmd" in query or "command prompt" in query:
            os.open_cmd()
        # to search wikepedia about something
        elif "wikipedia" in query: #sometime with searchable name prblm
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")#replacing the word "wikipedia" from query
            query=query.replace("Please","")
            query=query.replace("search","")
            query=query.replace("in","")
            query=query.replace("about","")
            query=query.replace("of","")
            results=on.search_on_wikipedia(query=query)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        # to get the ip 
        elif "ip" in query:
            ip=on.find_my_ip()
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")
        # to send email to someone
        elif "email" in query:
            # to get the dict from json format of emails.json file 
            with open("emails.json") as f:
                emails=json.loads(f.read())#here, emails is dictinory
            '''these for loop initialise name with a key of dictionary emails if that key is in the query'''

            """ye simply query se string extract karne ke liye h
            agr naam h emails dict mai toh vo naam "to" ko initialize hojayega varna for ke else part pe jaayega
            ab yaha pe 3 condition aata h:
            1.agr user ne query mai naam nhi diya
                ismai bhi 2 condition h:
                    1.agr jo naam dene wala h vo dict mai h:
                        toh phir vo else part mai jaayega aur udhr naam lene ke baad check hoga ki vo naam ab he ki nahi dict mai agr h toh vo email nhi puchega varna puchega
                    2.agr jo naam dene wala h vo dict nahi h:
                        agr nhi h toh else part mai jake vo naam aur email puch kr vo bhejdega email aur vo email ko phir add bhi kr lega json file mai
            2.agr user ne naam diya hua aur dict mai nahi h:
                ismai bhi vo else part mai jake same kaam karega
            3.agr user ne naam diya hua h aur dict mai h:
                ismai vo simplly for loop ke "to" mai initialize hoga aur else part ko skip karke try block mai chale jayega aur email bhej dega"""

            # loop for getting name of a receiver from query by comparing with emails dict
            for key in emails.keys():
                if key in query:
                    to=key
                    break
            # when name is not there in emails dict then it goes in these else block
            else:
                speak("We don't have a data of that person. Are you willing to give the data of that person")
                print("We don't have a data of that person. Are you willing to give the data of that person")
                res=takeCommand()   #confirmation for 
                if res=="yes":
                    speak("Sir,you have to give the data of that person manually for simplicity purpose!")
                    print("Sir,you have to give the data of that person manually for simplicity purpose!")
                    speak("What is the name of person,sir?")
                    to=input("Type the name of a person:")
                    if to in emails.keys():#checking again if the given name is in the dict or not
                        pass    #if name is there then it will directly go to try block for sending mail
                    else:
                        # here,Jazz will ask the email for sending mail and also add that new mail into emails dictinory
                        speak("What is the email of person,sir?")
                        Email=input("Type the email of person:")
                        emails[to]=Email    #update the emails dict
                        with open("emails.json","w") as f:
                            json.dump(emails,f,indent=4)    #dumping again the updated dictinory
                else:   #when ans is no then then it will continue the while loop
                    speak("Okay sir")
                    continue                    
            try:
                speak("What should be the subject of email?")
                subject=takeCommand()   #take subject of email
                speak("What should be the message,sir?")
                content=takeCommand()   #take message of email
                # to=[emails[name] for name in emails if name in query ]
                print(f"Email is been sending to {emails[to]}")
                speak(f"Email is been sending to {emails[to]}")
                speak("Please confirm this last time") 
                print("Say Yes or No!")
                confirmation=takeCommand()  #take comfirmation for sending the mail
                if confirmation=="yes":
                    on.send_email(emails[to],subject,content)   #calling function of send_email to send email with given data
                    print("Email has been sent!")
                    speak("Email has been sent!")
                else:
                    print("Please try again...")
                    speak("Please try again")
            except Exception as e:
                print(e)
                print("Sending email failed...")
                speak("Sorry,I am unable to send to the mail")

        # to here some news
        elif "news" in query:
            speak("I'm reading out the latest news headlines, sir")
            result=on.get_latest_news()
            # loop for printing the naame of movies line by line,not as list
            for title in result:
                print(title)
                speak(title)

        # to here some joke
        elif "joke" in query:
            speak("Hope you like this one sir")
            result=on.get_random_joke()
            print(result)
            speak(result)

        # to here some advice
        elif "advice" in query:
            speak("Here's an advice for you,sir")
            advice=on.get_random_advice()
            print(advice)
            speak(advice)
        # to get some trending movies name
        elif "trending movie" in query:
            movies=on.get_trending_movies()
            print(f"Some of the trending movies are:")
            for movie in movies:#same as trending movies
                print(movie)
            speak(f"Some of the trending movies are:{movies}")

        # to get the weather info of user location city
        elif 'weather' in query:
            ip_address = on.find_my_ip()#to get current ip address
            # to get the current city name
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            print(f"Getting weather report for your city {city}")
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = on.get_weather_report(city)
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")

        elif "hello" in query:
            speak("Hello Sir , I am Jazz. Your personal  AI assistant! How may I help you?")
        
        elif "how are you" in query:
            speak("I am fine sir! What about you ,sir?")
        elif "I am fine" in query:
            speak("Me too sir. What I can do for you ,Sir?")
        elif "take a break" in query:
            speak("Ok sir! You can call me anytime")
            break
        elif "kya haal hai" in query:
            speak("Main badiya hoon. App batao")
        elif "bye" in query:
            speak("Okay sir! Bye")
            break
        elif "search on youtube" in query:
            query=query.replace("search on youtube","")
            query=query.replace("Jazz","")
            on.search_on_youtube(query=query)
        elif "website" in query:
            query=query.replace("Jazz","")
            query=query.replace("website","")
            query=query.replace("search","")
            query=query.replace(".com","")
            query=query.replace("of","")
            on.search_website(query.strip()) 
        
        elif "message" in query:
            speak("Dhroov randi")
            speak("kaam kiya kya lavdae ,jo bola thaa madrchodh")
            speak("Maa ki chuhhuuuuu......")
            speak("Dhroov chuutiya , gaandu apna kaam kar lavdae")

        