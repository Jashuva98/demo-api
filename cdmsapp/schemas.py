from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class PlainEventSchema(Schema):
    event_id = fields.Int(dump_only=True)
    event_title = fields.Str(required=True)
    event_venue = fields.Str(required=True)
    event_address=fields.Str(required=True)
    event_state = fields.Str(required=True)
    event_district = fields.Str(required=True)
    event_date = fields.Str(required=True)
    event_time = fields.Str(required=True)

class TokenBlockListSchema(Schema):
    id = fields.Int(dump_only=True)
    jti = fields.Str(required=True)
    created_at = fields.Str(required=True)

class PlainParticipantSchema(Schema):
    id=fields.Int(dump_only=True)
    fullname = fields.Str(required=True)
    designation = fields.Str(required=True)
    email = fields.Str(required=True)
    mobilenumber = fields.Str(required=True)
    state = fields.Str(required=True)
    district = fields.Str(required=True)
    block = fields.Str(required=True)
    grampanchayat = fields.Str(required=True)

class ParticpantSchema(PlainParticipantSchema):
    event_id = fields.Int(required=True, load_only=True)
    event = fields.Nested(PlainEventSchema(), dump_only=True)

# External API models
class IndiaPincodeSchema(Schema):
    searchby = fields.Str()
    value = fields.Int()

class PincodeSchema(IndiaPincodeSchema):
    pin = fields.Int(required=True)
    office = fields.Str(required=True)
    office_type = fields.Str(required=True)
    delivery = fields.Str(required=True)
    devision = fields.Str(required=True)
    region = fields.Str(required=True)
    circle = fields.Str(required=True)
    taluk = fields.Str(required=True)
    district = fields.Str(required=True)
    state_id = fields.Str(required=True)
    phone = fields.Str(required=True)
    related_suboffice = fields.Str(required=True)
    related_headoffice = fields.Str(required=True)
    longitude = fields.Str(required=True)
    latitude = fields.Str(required=True)
    
    
class FeedbackSchema(Schema):
    feedback_id=fields.Int(dump_only=True)
    event_id = fields.Int(required=True, load_only=True)
    # name = fields.Str(required=True)
    # email = fields.Str(required=True)
    question1 = fields.Str(required=True)
    participant_id = fields.Int(required=True)
    # question2 = fields.Str(required=True)
    # question3 = fields.Str(required=True)
    data = fields.Str(required=True)
    

class EventSchema(PlainEventSchema):
    participants = fields.List(fields.Nested(PlainParticipantSchema()), dump_only=True)
    feedback = fields.List(fields.Nested(FeedbackSchema(), dump_only=True))