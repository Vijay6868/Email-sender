from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = 'saroyav3@gmail.com'
email_password = password

email_receiver = ''

subject = "email from vijay"

body = """
hi you received this email through python code
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['sub'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    
