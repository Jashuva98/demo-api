import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_smorest import Blueprint, abort


blp = Blueprint("PasswordEmail", "passwordemail", description="reset password email working")

def send_email12(subject, sender, recipients, body):
    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    # Add the body text to the message
    msg.attach(MIMEText(body, 'plain'))

    # Create an SMTP object and start TLS encryption
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.starttls()

    # Login to the SMTP server with your email address and app password
    # smtp_obj.login('kirankiru363@gmail.com', 'zsqwowpzednfpswb')
    smtp_obj.login('kirankiru363@gmail.com', 'zsqwowpzednfpswb')
    
    # Send the email and close the connection to the SMTP server
    smtp_obj.sendmail(sender, recipients, msg.as_string())
    smtp_obj.quit()

    return {'message': 'Email sent successfully!'}
