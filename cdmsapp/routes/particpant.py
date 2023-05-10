
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask import request

from cdmsapp.schemas import ParticpantSchema
from cdmsapp.models import ParticipantModel


blp = Blueprint("Participants", "participants", description="Operations on participants")

@blp.route("/register/participant")
class InsertParticipant(MethodView):
    @blp.arguments(ParticpantSchema)
    def post(self, participant_data):
        # if ParticipantModel.find_by_mobilenumber(mobile=participant_data['mobilenumber']):
        #     abort(400, "Mobile Number already exists")
        participant = ParticipantModel(
            event_id = participant_data['event_id'],
            fullname = participant_data['fullname'],
            designation = participant_data['designation'],
            email = participant_data['email'],
            mobilenumber = participant_data['mobilenumber'],
            state = participant_data['state'],
            district = participant_data['district'],
            block = participant_data['block'],
            grampanchayat = participant_data['grampanchayat']
        )

        participant.save_to_db()

        return {"message":"Participant registered successfully"}, 201 

@blp.route('/modify/participant')
def UpdateParticipant(MethodView):
    @blp.arguments(ParticpantSchema)
    def post(self, participant_data):
        if not ParticipantModel.find_by_mobilenumber(mobile=participant_data['mobilenumber']).first():
            participant = ParticipantModel(
                fullname = participant_data['fullname'],
                designation = participant_data['designation'],
                email = participant_data['email'],
                mobilenumber = participant_data['mobilenumber'],
                state = participant_data['state'],
                district = participant_data['district'],
                block = participant_data['block'],
                grampanchayat = participant_data['grampanchayat']
            )
            participant.save_to_db()
        else:
            abort(400, "Participant does not exists")

@blp.route("/participant/<int:participant_id>")
class User(MethodView):
    """
    This resource can be useful when testing our Flask app.
    We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful
    when we are manipulating data regarding the users.
    """

    @blp.response(200, ParticpantSchema)
    # @jwt_required(refresh=True)
    def get(self, participant_id):
        participant = ParticipantModel.find_by_id(participant_id)
        if not participant:
            abort(404, message="Participant not found.")
        return participant

    def delete(self, participant_id):
        participant = ParticipantModel.find_by_id(participant_id)
        if not participant:
            abort(404, message="Participant not found.")
        participant.delete_from_db()
        return {"message": "Participant deleted."}, 200 
    ''' 
    @blp.arguments(ParticpantSchema)
    @blp.response(200,ParticpantSchema)
    def put(self, data, participant_id):
        participant = ParticipantModel.find_by_id(participant_id)
        if participant is None:
            participant = ParticipantModel( 
                participant_id=id,
                fullname=data['fullname'],
                email=data['email'],
                designation=data['designation'],
                mobilenumber = data['mobilenumber'],
                state = data['state'],
                district = data['district'],
                block = data['block'],
                grampanchayat = data['grampanchayat'])
        else:
            participant =ParticipantModel (
                participant_id=id,
                fullname=data['fullname'],
                email=data['email'],
                designation=data['designation'],
                mobilenumber = data['mobilenumber'],
                state = data['state'],
                district = data['district'],
                block = data['block'],
                grampanchayat = data['grampanchayat'])

        participant.update_to_db()
        # return item.json()

        return {"message": "participant updated successfully"}, 201
    '''
    def put(self,participant_id):
        data = request.get_json()
        participant = ParticipantModel.find_by_id(participant_id)
        if participant:
            # participant.event_id = data['event_id'],
            participant.fullname = data['fullname'],
            participant.email = data['email'],
            participant.designation = data['designation'],
            participant.mobilenumber = data['mobilenumber'],
            participant.state = data['state'],
            participant.district = data['district'],
            participant.grampanchayat = data['grampanchayat'],
            participant.block = data['block']
        else:
            participant = ParticipantModel(id=participant_id,**data)
        participant.save_to_db()
        
        return participant.json()
      

# @blp.route('/delete/participant')

# @blp.route('/get/all/paticipants')

# @blp.route('get/participant')

@blp.route("/participants")
class ItemList(MethodView):
    # @jwt_required(refresh=True)
    @blp.response(200, ParticpantSchema(many=True))
    def get(self):
        participants = ParticipantModel.get_all_participants()
        # for _event in events:
        #     _event_date = dt(day=int(_event['event_date'].split('-')[2]),month=int(_event['event_date'].split('-')[1]),year=int(_event['event_date'].split('-')[0]))
        #     _event['event_date'] = _event_date
        return participants
