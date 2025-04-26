import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from decouple import config


def send_email(name, dest, link):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail SMTP port (TLS)
    server.starttls()

    # Load credentials from .env
    email_user = config('EMAIL_HOST_USER')
    email_password = config('EMAIL_HOST_PASSWORD')
    default_from_email = config('DEFAULT_FROM_EMAIL')

    server.login(email_user, email_password)

    email_html = open("main_app/templates/main_app/email.html")
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg["Subject"] = "EMERGENCY"
    msg.attach(MIMEText(email_body, "html"))

    msg["From"] = formataddr(("TEAM HerSheild", default_from_email))

    server.sendmail(default_from_email, dest, msg.as_string())
    server.quit()
