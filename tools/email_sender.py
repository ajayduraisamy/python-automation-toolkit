from email.message import EmailMessage
import smtplib

def send_email(sender, password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print(" Email sent successfully")

if __name__ == "__main__":
    print("Run this after adding real login credentials")
