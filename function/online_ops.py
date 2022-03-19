from email.message import EmailMessage
import wikipedia
from decouple import config
import smtplib



EMAIL=config("EMAIL")
PASSWORD=config("PASSWORD")


def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentences=2)
    return results

# def search_on_google(query):
def send_email(receiver_address, subject, message):
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
