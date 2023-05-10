from cdmsapp.extensions import db
import uuid

class EventModel(db.Model):
    __tablename__ = "events"

    event_id = db.Column(db.BigInteger, primary_key=True)
    event_title = db.Column(db.String(256), nullable=False)
    event_venue = db.Column(db.String(256), nullable=False)
    event_address = db.Column(db.String(256), nullable=False)
    event_state = db.Column(db.String(250),nullable=False)
    event_district = db.Column(db.String(256),nullable=False)
    event_date = db.Column(db.String(128), nullable=False)
    event_time = db.Column(db.String(128), nullable=False)
    created_by = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.String(),nullable=False)
    
    participants = db.relationship("ParticipantModel", back_populates="event", lazy="dynamic")
    feedback = db.relationship("FeedbackModel",back_populates="event",lazy="dynamic")


    def json(self):
        return {
            'id': int(uuid.uuid4().int & (2**31-1)),
            'event_title': self.event_title,
            'event_venue': self.event_venue,
            'event_address': self.event_address,
            'event_state':self.event_state,
            'event_district':self.event_district,
            'event_date': self.event_date,
            'event_time': self.event_time,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d-%m-%Y %H:%M:%S'),
        }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(event_title=title).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(event_id=_id).first()
    
    @classmethod
    def get_all_events(cls):
        array1= cls.query.all()
        print(array1)
        return array1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, event_data):
        event = self.find_by_id(event_data.event_id)
        event.event_address= event_data.event_address
        event.event_venue=event_data.event_venue
        event.event_date=event_data.event_date
        event.event_time=event_data.event_time
        event.event_title=event_data.event_title
        db.session.add(event)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()