from app import db

class User(db.Model):
    __tablename__='users'
    id = db.Column()
    user_acess
    password
    user_name
    user_email