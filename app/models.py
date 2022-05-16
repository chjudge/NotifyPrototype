from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=False)
    last_name = db.Column(db.String(40), unique=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(10), unique=True)
    state = db.Column(db.String(40), unique=False)
    county = db.Column(db.String(40), unique=False)
    zipcode = db.Column(db.String(40), unique=False)
    precinct = db.Column(db.String(40), unique=False)
    party = db.Column(db.String(40), unique=False)
    voter = db.Column(db.Boolean, unique=False)
    interest = db.Column(db.String(40), unique=False)

    def __init__(self, first_name, last_name, email, phone, state, county, zipcode, precinct, party, voter, interest):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.state = state
        self.county = county
        self.zipcode = zipcode
        self.precinct = precinct
        self.party = party
        self.voter = voter
        self.interest = interest


    def __repr__(self):
        return '<User %r>' % self.email