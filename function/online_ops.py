from email.message import EmailMessage
import wikipedia
from decouple import config
import smtplib
import requests
import webbrowser



EMAIL=config("EMAIL")
PASSWORD=config("PASSWORD")
NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHERMAP_API_KEY=config("OPENWEATHERMAP_API_KEY")
TMDB_USER_API_KEY=config("TMDB_USER_API_KEY")

# function for searching query in wikipedia
def search_on_wikipedia(query):
    # works in other comps
    results=wikipedia.summary(query,sentences=2)
    return results

# def search_on_google(query):
#     kit.search(query)

def search_on_youtube(query):
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_website(query):
    print(query)
    url="https://"+query+".com"
    webbrowser.open(url)

# function for getting ip 
# it is online function 
def find_my_ip():
    # works in other comps
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
    
# for getting the latest news
def get_latest_news():
    # needs API key 
    news_headlines = []
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

# for sending email
def send_email(receiver_address, subject, message):
    # works in other comps
    try:
        email = EmailMessage()
        email["To"] = receiver_address
        email["Subject"] = subject
        email["From"] = EMAIL
        email.set_content(message)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(email)
        server.close()
        return True
    except Exception as e:
        print(e)
        return False

# fo getting jokes
def get_random_joke():
    # works in other comps
    headers = {"Accept": "application/json"}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

# for getting advice
def get_random_advice():
    # works in other comps
    res=requests.get("https://api.adviceslip.com/advice").json()
    return res["slip"]["advice"]

def get_weather_report(city):
    # need API key 
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric").json()
    weather=res["weather"][0]["main"]
    temperature=res["main"]["temp"]
    feels_like=res["main"]["feels_like"]
    return weather,f"{temperature}??C",f"{feels_like}??C"

def get_trending_movies():
    # need API key
    trending_movies=[]
    res=requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_USER_API_KEY}").json()
    results=res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5] 