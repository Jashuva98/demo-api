
import json
from flask import jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import requests
from cdmsapp.models import pincodeModel
from cdmsapp.models.pincodes import pincode



from cdmsapp.schemas import IndiaPincodeSchema
from cdmsapp.schemas import PincodeSchema


blp = Blueprint("external", "externals", description="Operations on external apis")

@blp.route("/external/pincode")
class IndiaPincode(MethodView):
    @blp.arguments(IndiaPincodeSchema)
    def post(self, _payload):
        url = "https://pincode.p.rapidapi.com/"
        payload = pincodeModel()
        payload.searchby = "pincode"
        payload.value = _payload['value']
        json_payload = {
            "searchBy": payload.searchby,
            "value": payload.value
        }

        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "c4b7a5db43msh73ce9d48e29aaa6p1de149jsnfccde7fc5c45",
            "X-RapidAPI-Host": "pincode.p.rapidapi.com"
        }
        #first check in the our own database and return
    # write code here for checking in the local database */
    # if it is not available in the database check from rapid api
        try:
            response = requests.request("POST", url, json=json_payload, headers=headers)
            return_json = json.loads(response.text)
            print(response.text)
            for data in response:
                codes = pincode(
                        pin = data['pin'],
                        office = data['office'],
                        office_type = data['office_type'],
                        delivery = data['delivery'],
                        devision = data['devision'],
                        region = data['region'],
                        circle = data['circle'],
                        taluk = data['taluk'],
                        district = data['district'],
                        state_id = data['state_id'],
                        phone = data['phone'],
                        related_suboffice = data['related_suboffice'],
                        related_headoffice = data['related_headoffice'],
                        longitude = data['longitude'],
                        latitude = data['latitude'],
                    )

                codes.save_to_db()
            # write code for inserting  the dictionary in the local database
            # for loop to iterate through each data
        except:
            return {"message":"failure"}

        return return_json[0]

# home url = "https://rapidapi.com/navii/api/pin-codes-india"
