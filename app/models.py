class Wishlist(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    title           = db.Column(db.String(200))
    description     = db.Column(db.String(5000))
    url             = db.Column(db.String(500))
    thumbnail       = db.Column(db.String(500))
    userid          = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Item %r>' % self.title    


class Profile(db.Model):
    username    = db.Column(db.String(30),primary_key=True)
    userid      = db.Column(db.Integer)
    firstname   = db.Column(db.String(30))
    lastname    = db.Column(db.String(30))
    image       = db.Column(db.String(30))
    sex         = db.Column(db.String(6))
    age         = db.Column(db.Integer)
    profile_added_on = db.Column(db.DateTime)

    def __repr__(self):
        return'<Profile %r>' % self.username
        
#Noot finish 