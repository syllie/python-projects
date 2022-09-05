import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from pathlib import Path
from string import Template


def configure():
    load_dotenv()


def main():
    configure()

    html = Template(Path('index.html').read_text())

    email = EmailMessage()
    email['from'] = 'from@example.com'
    email['to'] = 'to@example.com'
    email['subject'] = 'Keep on coding!'

    email.set_content(html.substitute({'name': 'Ada Lovelace'}), 'html')

    with smtplib.SMTP(f"{os.getenv('EMAIL_HOST')}", f"{os.getenv('EMAIL_PORT')}") as server:
        server.ehlo()
        server.starttls()
        server.login(f"{os.getenv('EMAIL_HOST_USER')}",
                     f"{os.getenv('EMAIL_HOST_PASSWORD')}")
        server.send_message(email)
        print('all good!')


main()
