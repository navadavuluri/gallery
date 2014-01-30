from app import models, db

I1 = models.Image(desc="Waves!", image="../static/images/bigsur.jpg", lat=121, lon=234, addr="123 Ocean Ave, Big Sur, CA")
I2 = models.Image(desc="Water!", image="../static/images/burano.jpg", lat=121, lon=234, addr="123 Ocean Ave, Milan, Italy")
I3 = models.Image(desc="Wind", image="../static/images/eastbay.jpg", lat=121, lon=234, addr="123 Ocean Ave, East Bay, CA")
I4 = models.Image(desc="Like", image="../static/images/fb.jpg", lat=121, lon=234, addr="123 Ocean Ave, Palo Alot, CA")
I5 = models.Image(desc="Dome", image="../static/images/halfdome.jpg", lat=121, lon=234, addr="123 Ocean Ave, Half Dome, CA")
I6 = models.Image(desc="Street", image="../static/images/italy.jpg", lat=121, lon=234, addr="123 Ocean Ave, Milan, Italy")
I7 = models.Image(desc="Hill", image="../static/images/sc.jpg", lat=121, lon=234, addr="123 Hill Ave, Santa Cruz, CA")
I8 = models.Image(desc="City", image="../static/images/sf.jpg", lat=121, lon=234, addr="123 Ocean Ave, San Francisco, CA")

photos = [I1, I2, I3, I4, I5, I6, I7, I8]

for photo in photos:
	db.session.add(photo)
	db.session.commit()
