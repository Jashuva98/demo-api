from cdmsapp.extensions import db

class pincode(db.Model):
    __tablename__ = "pincodes"

    id = db.Column(db.Integer, primary_key=True)
    circle =  db.Column(db.String, unique=False, nullable=False)
    delivery =  db.Column(db.String, unique=False, nullable=False)
    district =  db.Column(db.String, unique=False, nullable=False)
    division =  db.Column(db.String, unique=False, nullable=False)
    latitude =  db.Column(db.String, unique=False, nullable=False)
    longitude =  db.Column(db.String, unique=False, nullable=False)
    office =  db.Column(db.String, unique=False, nullable=False)
    office_type =  db.Column(db.String, unique=False, nullable=False)
    phone =  db.Column(db.String, unique=False, nullable=False)
    pin =  db.Column(db.String, unique=False, nullable=False)
    region =  db.Column(db.String, unique=False, nullable=False)
    state_id =  db.Column(db.String, unique=False, nullable=False)
    related_headoffice =  db.Column(db.String, unique=False, nullable=False)
    related_suboffice =  db.Column(db.String, unique=False, nullable=False)
    taluk =  db.Column(db.String, unique=False, nullable=False)


#   "": "Delivery",
#   "": "Dakshina Kannada",
#   "": "Mangalore",
#   "": "Not Available",
#   "": "Not Available",
#   "": "Shakthinagar (Dakshina Kannada) S.O",
#   "": "S.O",
#   "": "0824-2232076",
#   "": 575016,
#   "": "South Karnataka",
#   "": "Kulshekar H.O",
#   "": "Not Available",
#   "": 15,
#   "": "Mangalore"
# state
# state_id

# district
# district_id
# state_id

# taluk
# taluk_id
# district_id


# {
#   "circle": "Karnataka",
#   "delivery": "Delivery",
#   "district": "Dakshina Kannada",
#   "division": "Mangalore",
#   "latitude": "Not Available",
#   "longitude": "Not Available",
#   "office": "Shakthinagar (Dakshina Kannada) S.O",
#   "office_type": "S.O",
#   "phone": "0824-2232076",
#   "pin": 575016,
#   "region": "South Karnataka",
#   "related_headoffice": "Kulshekar H.O",
#   "related_suboffice": "Not Available",
#   "state_id": 15,
#   "taluk": "Mangalore"
# }
    def json(self):
        return {
            'id':self.id,
            'circle':self.circle,
            'delivery':self.delivery,
            'district':self.district,
            'devision':self.division,
            'latituide':self.latitude,
            'longituide':self.longitude,
            'office':self.office,
            'office_type':self.office_type,
            'phone':self.phone,
            'pin':self.pin,
            'region':self.region,
            'related_suboffice':self.related_suboffice,
            'related_headoffice':self.related_headoffice,
            'state_id':self.state_id,
            'taluk':self.taluk
        }

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
