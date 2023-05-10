from cdmsapp.extensions import db

class FeedbackModel(db.Model):
    __tablename__ = 'feedback'

    feedback_id = db.Column(db.Integer,primary_key=True)
    # name = db.Column(db.String(),nullable=True)
    # email = db.Column(db.String(),nullable=True)
    question1 = db.Column(db.String(),nullable=True)
    # question2 = db.Column(db.String(),nullable=True)
    # question3 = db.Column(db.String(),nullable=True)
    participant_id = db.Column(db.Integer,nullable=False)
    data = db.Column(db.String(),nullable=True)

    event_id = db.Column(db.Integer, db.ForeignKey("events.event_id"), unique=False, nullable=False)
    event = db.relationship("EventModel",back_populates="feedback")    

    # id = db.Column(db.Integer,db.ForeignKey("participants.id"))
    # feedback = db.relationship("ParticipantModel",back_populate="participant")

    def json(self):
        return {
            'feedback_id':self.feedback_id,
            # 'name':self.name,
            # 'email':self.email,
            'question1':self.question1,
            # 'question2':self.question2,
            # 'question3':self.question3,
            'participant_id':self.participant_id,
            'data':self.data,
            'event_id':self.event_id
    }
        
    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(feedback_id=id).first()
    
    @classmethod
    def get_all_feedback(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
