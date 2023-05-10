from flask import Flask,request,send_file,jsonify
import qrcode
import io
from flask_smorest import Blueprint, abort

blp = Blueprint("Qrcode", "qrcode", description="Qrcode generating")


@blp.route('/qrcode/<int:event_id>',methods=['POST'])
def generate_qrcode(event_details):
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(f'localhost:4200/participant/register/event/{event_id}')
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black",back_color="white")
    file =io.BytesIO()
    img.save(file,'PNG')
    file.seek(0)
    
    return send_file(file,mimetype='image/PNG')

    

