import smtplib
import os
from email.mime.text import MIMEText
from typing import Optional

def send_email(to_email: str, subject: str, body: str, 
                smtp_server: str = "live.smtp.mailtrap.io",
                port: int = 587, 
                login: str = "api", 
                password: str = os.getenv("PASSWORD"), 
                from_email: str = os.getenv("EMAIL")):
    message = MIMEText(body, "plain")
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls() 
            server.login(login, password)
            server.sendmail(from_email, to_email, message.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')




send_email(
    to_email="new@example.com",
    subject="Plain text email",
    body="""\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!
"""
)
