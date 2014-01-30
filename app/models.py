from app import db
import json

class Image(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        desc = db.Column(db.String(120), unique=False)
        image = db.Column(db.String(256), unique=False)
        lat = db.Column(db.Float, index = True, unique=False)
        lon = db.Column(db.Float, index = True, unique=False)
	addr = db.Column(db.String(128), unique=False)

	def json(self):
		return {"id": self.id, "desc": self.desc, "image": self.image, "lat": self.lat, "lon": self.lon, "addr": self.addr}	

'''        def __repr__(self):
                return '<description %r>' % (self.desc)'''

