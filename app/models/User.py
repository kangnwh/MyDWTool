from app.models import db


class User(db.Model):
    __tablename__= 'users'
    __table_args__ = {'schema':'mydwtool'}
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(255), unique = True)
    role = db.Column(db.String(255), default = 'public')

    def __init__(self,id,nickname,email,password,role='public'):
        self.id = id
        self.nickname = nickname
        self.email = email
        self.password = password
        self.role = role


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.nickname)