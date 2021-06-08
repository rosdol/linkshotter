from app import db
from hashids import Hashids

hashids = Hashids()

class ShortedLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(64), unique=True)
    long_url = db.Column(db.String(128))

    def set_token(self, token):
        if token == '':
            token = hashids.encode(self.id)
        self.token = token


    def __repr__(self):
        return '<User {}>'.format(self.token)
