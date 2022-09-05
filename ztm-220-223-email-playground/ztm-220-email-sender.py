import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


def configure():
    load_dotenv()


def main():
    configure()

    email = EmailMessage()
    email['from'] = 'from@example.com'
    email['to'] = 'to@example.com'
    email['subject'] = 'Keep on coding!'

    email.set_content('I am a Python coder!')

    with smtplib.SMTP(f"{os.getenv('EMAIL_HOST')}", f"{os.getenv('EMAIL_PORT')}") as server:
        server.ehlo()
        server.starttls()
        server.login(f"{os.getenv('EMAIL_HOST_USER')}",
                     f"{os.getenv('EMAIL_HOST_PASSWORD')}")
        server.send_message(email)
        print('all good!')


main()
