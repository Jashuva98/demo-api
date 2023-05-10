import smtplib
from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from flask_smorest import Blueprint, abort
from smtplib import SMTP


blp = Blueprint("Mail","mail", description="send email is working")



        



@blp.route('/send_email', methods=['POST'])
def send_email():
    # Extract data from the POST request
    data = request.get_json()
    to_emails = data.get('to')
    title = data.get('title')
    body = data.get('body')

    # Create the email message
    message = f"Subject: {title}\n\n{body}"

    # Send the email using SMTP
    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login('kirankiru363@gmail.com', 'xhsnifhukqodqwov')
        smtp_obj.sendmail('kirankiru363@gmail.com', to_emails, message)
        smtp_obj.quit()
        return jsonify({'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})