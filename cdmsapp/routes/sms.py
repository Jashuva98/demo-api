from flask import Flask, request, jsonify
from flask_smorest import Blueprint, abort
import urllib.request
import urllib.parse
import requests


blp = Blueprint("Sms", "sms", description="send sms is working")



# @blp.route('/send_sms', methods=['POST'])
# def send_sms():
#     api_key = 'NzI3NzRmNTk0NjY2NTY0ZTc3Njg0Zjc2NTg2MzY5NzI='
#     sender = ''  # optional, can be left blank
#     url = 'https://api.textlocal.in/send/'


#     data = request.get_json()
#     mobile_number = '+91' + str(data.get('mobile_number'))
#     # mobile_number = data.get('mobile_number')
#     message_body = data.get('message_body')
#     print('Mobile number:', mobile_number)

#     params = {
#         'apiKey': api_key,
#         'sender': sender,
#         'numbers': mobile_number,
#         'message': message_body
#     }

#     response = requests.post(url, data=params)
#     if response.status_code == 200:
#         return 'Message sent successfully'
#     else:
#         return 'Error sending message'
    

@blp.route('/send_sms', methods=['POST'])
def send_sms():
    apikey = 'NzI3NzRmNTk0NjY2NTY0ZTc3Njg0Zjc2NTg2MzY5NzI='
    sender = ''

    data = request.get_json()
    numbers = data.get('numbers')
    message = data.get('message')
    # otp = 123456
    # message = 'Thank you for registering with RTM. Please enter the verification code {otp} to complete the registration.'
    # message = urllib.parse.quote(message)
    
   
 
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    req = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(req, data)
    response = f.read()
 
    return response









