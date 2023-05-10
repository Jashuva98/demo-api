from cdmsapp.extensions import db

class ParticipantModel(db.Model):
    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(), nullable=False)
    designation = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(),  nullable=False)
    mobilenumber = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    district = db.Column(db.String(), nullable=False)
    block = db.Column(db.String(), nullable=False)
    grampanchayat = db.Column(db.String(), nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey("events.event_id"), unique=False, nullable=False)

    event = db.relationship("EventModel", back_populates="participants")
    
    

    def json(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'designation': self.designation,
            'email': self.email,
            'mobilenumber': self.mobilenumber,
            'state': self.state,
            'district': self.district,
            'block': self.block,
            'grampanchayat': self.grampanchayat,
            'event_id': self.event_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_all_participants(cls):
        return cls.query.all()

    @classmethod
    def find_by_mobilenumber(cls, mobile):
        return cls.query.filter_by(mobilenumber=mobile).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

#     def update_to_db(self, cls):
#         participant = cls.query.filter_by(id=self.id)

#         if participant == None:
#             return None

#         participant.update({

#         })
    def update_to_db(self, participant_data):
        participant = self.find_by_id(participant_data.id)
        participant.fullname= participant_data.fullname
        participant.email=participant_data.email
        participant.designation=participant_data.designation
        participant.mobilenumber=participant_data.mobilenumber
        participant.state=participant_data.state
        participant.district=participant_data.district
        participant.grampanchayat=participant_data.grampanchayat
        participant.block=participant_data.block
        db.session.add(participant)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
