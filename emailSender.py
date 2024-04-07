from email.message import EmailMessage
import os
from dotenv import load_dotenv # Import dotenv
import ssl
import smtplib
# loading the env from .env file
load_dotenv()

email_sender = 'sender@gmail.com'
# Get the email password from the env
email_password = os.getenv("EMAIL_PASSWORD")

email_receiver = 'receiver@gmail.com'

subject = "Hello I am Shushant"
body = """
    I am Rohit Verma. I am 2nd year Btech student pursuing computer science.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())