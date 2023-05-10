from cdmsapp.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime
from flask import current_app
from datetime import timedelta,datetime
from werkzeug.security import generate_password_hash, check_password_hash




class UserModel(db.Model):
    __tablename__ = "users"

    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }
     

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def verify_email(cls,username):
        user = cls.query.filter_by(username=username).first()

        return user
    
    @classmethod
    def get_all_user(cls):
        return cls.query.all()

    def verify_reset_password_token(token):
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            # user_id = data['reset_password']
            user_id = data['user_id']
            print(user_id)
        except:
            return None
        return user_id

  


    def generate_reset_password_token(self):
        try:
            # Set the expiration time for the token (e.g. 1 hour)
            expiration_time = datetime.utcnow() + timedelta(hours=1)

            # Create the payload for the token
            payload = {
                'user_id': self.id,
                'exp': expiration_time
            }

            # Encode the payload with a secret key to generate the token
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
            print(token)

            return token

        except Exception as e:
            print(e)
            return None


    


   
       
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

  




    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



