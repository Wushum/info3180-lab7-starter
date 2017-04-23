from . import db

class Wishlist(db.Model):
    id              = db.Column(db.Integer, primary_key = True)
    userid          = db.Column(db.Integer, db.ForeignKey('user.id'))
    title           = db.Column(db.String(200))
    description     = db.Column(db.String(5000))
    url             = db.Column(db.String(500))
    thumbnail       = db.Column(db.String(500))
    created_on = db.Column(db.DateTime)
    
    def __init__(self, userid, title, description, url, thumbnail, created_on):
        self.userid = userid        
        self.title = title
        self.description = description
        self.url = url
        self.thumbnail = thumbnail
        self.created_on = created_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
            
    def __repr__(self):
        return '<Wishlist %r>' % self.title    


class Profile(db.Model):
    userid = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(30), unique=True, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    gender = db.Column(db.String(6))
    password = db.Column(db.String(255))
    profile_added_on = db.Column(db.DateTime)
    
    def __init__(self, userid, username, firstname, lastname, email, gender, password, profile_added_on):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.password = password
        self.profile_added_on = profile_added_on
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
        
    def __repr__(self):
        return'<Profile %r>' % self.username
        
#Complete