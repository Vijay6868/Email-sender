from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = '<your_email_address_here>'
email_password = password

email_receiver = 'jotefey546@lendfash.com'

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
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    
