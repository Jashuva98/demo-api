from flask.views import MethodView
from flask import request
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_smorest import Blueprint, abort
from datetime import time as tm, date as dt
import uuid
from cdmsapp.schemas import EventSchema
from cdmsapp.models import EventModel
from cdmsapp.models import UserModel
from datetime import datetime


blp = Blueprint("Events", "events", description="Operations on events")

# @blp.route("/events")
# class GetAllEvents(MethodView):
#     @blp.response(200, EventSchema)
#     def getall(self):
#         events = EventModel.query.all()
#         return {
#             'events':list(x.json() for x in events)
#         }
#         # if not events:
#         #     abort(404, message="Events not found.")
#         # return events

# # Insert Event into db

# @blp.route("/events")
# class getAll(MethodView):
#     @blp.response(200,EventSchema)
#     def getAll(self):
#         events = EventModel.query.all()
#         return {'events':list(x.json() for x in events)}



@blp.route("/event/registration")
class InsertEvent(MethodView):
    @blp.arguments(EventSchema)
    @jwt_required(refresh=True)
    def post(self, event_data):
        current_user = UserModel.find_by_id(get_jwt_identity())
        if not current_user:
            abort(404,'user not found')
        # if EventModel.find_by_title(title=event_data['event_title']):
        #     abort(400, "Mobile Number already exists")
        _event_date = dt(
            year=int(event_data['event_date'].split('-')[0]),
            month=int(event_data['event_date'].split('-')[1]),
            day=int(event_data['event_date'].split('-')[2])),
        _event_time = tm(int(event_data['event_time'].split(':')[0]), int(
            event_data['event_time'].split(':')[1]), 0, 0)
        event_ = EventModel(
            event_title=event_data['event_title'],
            event_venue=event_data['event_venue'],
            event_address=event_data['event_address'],
            event_state =event_data['event_state'],
            event_district = event_data['event_district'],
            event_date=_event_date,
            event_time=_event_time,
            created_by = current_user.username,
            created_on = datetime.now()
        )
        print(event_.event_id),
        event_id = int(uuid.uuid4().int & (2**31-1))
        event_.event_id = event_id
        # for testing purpose use print command and comment the save_to_db.
        # print(event_.event_date.today().ctime())
        event_.save_to_db()

        return {"message": "Event registered successfully"}, 201

# Update event in the db

'''
@blp.route("/event/update")
class UpdateEvent(MethodView):
    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def put(self, data, event_id):
        # data = Event.parser.parse_args()
        event = EventModel.find_by_id(event_id)
        if event is None:
            _event_date = dt(
                day=int(data['event_date'].split('-')[2]),
                month=int(data['event_date'].split('-')[1]),
                year=int(data['event_date'].split('-')[0]))
            _event_time = tm(int(data['event_time'].split(':')[0]), int(
                data['event_time'].split(':')[1]), 0, 0)
            event = EventModel(
                event_id=data['event_id'],
                event_title=data['event_title'],
                event_address=data['event_address'],
                event_time=_event_time,
                event_date=_event_date,
                event_venue=data['event_venue'])
        else:
            _event_date = dt(
                day=int(data['event_date'].split('-')[2]),
                month=int(data['event_date'].split('-')[1]),
                year=int(data['event_date'].split('-')[0]))
            _event_time = tm(int(data['event_time'].split(':')[0]), int(
                data['event_time'].split(':')[1]), 0, 0)
            event = EventModel(
                event_id=data['event_id'],
                event_title=data['event_title'],
                event_address=data['event_address'],
                event_time=_event_time,
                event_date=_event_date,
                event_venue=data['event_venue'])

        event.update_to_db()
        # return item.json()

        return {"message": "Event updated successfully"}, 201
'''
# get event or delete event by id


@blp.route("/event/<int:event_id>")
class Event(MethodView):

    @blp.response(200, EventSchema)
    def get(self, event_id):
        event = EventModel.find_by_id(event_id)
        if not event:
            abort(404, message="Event not found.")
        return event

    def delete(self, event_id):
        event = EventModel.find_by_id(event_id)
        if not event:
            abort(404, message="Event not found.")
        event.delete_from_db()
        return {"message": "Event deleted."}, 200

    @blp.arguments(EventSchema)
    # @blp.response(200, EventSchema)
    def put(self, data, event_id):
        # data = Event.parser.parse_args()
        event = EventModel.find_by_id(event_id)
        if event is None:
            event = EventModel(
                event_id=event_id,
                event_title=data['event_title'],
                event_address=data['event_address'],
                event_state =data['event_state'],
                event_district = data['event_district'],
                event_time=data['event_time'],
                event_date=data['event_date'],
                event_venue=data['event_venue'])
        else:
            event = EventModel(
                event_id=event_id,
                event_title=data['event_title'],
                event_address=data['event_address'],
                event_state =data['event_state'],
                event_district = data['event_district'],
                event_time=data['event_time'],
                event_date=data['event_date'],
                event_venue=data['event_venue'])

        event.update_to_db(event)
        # event.save_to_dbO()
        # return event.json()
        # return item.json()

        return {"message": "Event updated successfully"}, 201
    
    # def put(self,event_id):
    #     data = request.get_json()
    #     event = EventModel.query.filter_by(id = event_id).first()
    #     if event:
    #         event.event_title = data['event_title'],
    #         event.event_address = data['event_address'],
    #         event.event_time = data['event_time'],
    #         event.event_date = data['event_date'],
    #         event.event_venue = data['event_venue']
    #     else:
    #         event = EventModel(id=event_id,**data)
    #     event.save_to_db()
    #     return event.json()

# get all event


@blp.route("/events")
class ItemList(MethodView):
    # @jwt_required(refresh=True)
    @blp.response(200, EventSchema(many=True))
    def get(self):
        events = EventModel.get_all_events()
        if events is None:
            abort(404,message="No Events Found")
        return events

    # @jwt_required(fresh=True)
    @blp.arguments(EventSchema)
    @blp.response(201, EventSchema)
    def post(self, event_data):
        item = EventModel(**event_data)
        item.save_to_db()
        # try:
        #     db.session.add(item)
        #     db.session.commit()
        # except SQLAlchemyError:
        #     abort(500, message="An error occurred while inserting the item.")

        return item
    
    
