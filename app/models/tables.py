from app import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Interger, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    user_email= db.Column(db.String, unique=True)

    def __init__(self,user_name,password,name,user_email):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.user_email= user_email

    def __repr__(self):
        return '<User %r>' %self.user_name


class Client(db.Model):
    __tablename__='clients'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Integer, unique=True)
    client_name = db.Column(db.String)
    date_birth = db.Column(db.DateTime)
    phone_primary = db.Column(db.Integer)
    phone_secundary = db.Column(db.Integer)
    client_email = db.Column(db.String)
    cep = db.Column(db.Integer)

    def __init__(self,cpf,client_name,date_birth,phone_primary,phone_secundary,client_email,cep):
        self.cpf = cpf
        self.client_name = client_name
        self.date_birth = date_birth
        self.phone_primary = phone_primary
        self.phone_secundary = phone_secundary
        self.client_email = client_email
        self.cep = cep
    
    def __repr__(self):
        return '<Client %r>' %self.client_name


class Doctor(db.Model):
    __tablename__='doctors'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Integer, unique=True)
    user_email = db.Column(db.String, unique=True)
    cep = db.Column(db.Integer, unique=True)
    doctor_name = db.Column(db.String)
    specialty_name = db.Column(db.String)
    date_birth = db.Column(db.DateTime)
    phone_primary = db.Column(db.Integer)
    phone_secundary = db.Column(db.Integer)
    doctor_email = db.Column(db.String)
    user_name = db.Column(db.String)
    
    def __init__(self,cpf,user_email,cep,doctor_name,specialty_name,date_birth,phone_primary,phone_secundary,doctor_email,user_name):
        self.cpf = cpf
        self.user_email = user_email
        self.cep = cep
        self.doctor_name = doctor_name
        self.specialty_name = specialty_name
        self.date_birth = date_birth
        self.phone_primary = phone_primary
        self.phone_secundary = phone_secundary
        self.doctor_email = doctor_email
        self.user_name = user_name

    def __repr__(self):
        return '<Doctor %r>' %self.doctor_name


class Specialty (db.Model):
    __tablename__='specialtys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    

    def __init__(self,name,description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return '<Specialty %r>' %self.name
    

class  Occupation_area (db.Model):
    __tablename__='occupation_areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    doctor_response_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor_data = db.relationship('Doctors', foreing_keys=doctor_response_id)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialtys.id'))
    specialty_data = db.relationship('Specialty', foreing_keys=specialty_id)
    cep = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.String)

    def __init__(self,name,doctor_response_id,doctor_data,cep,price,description):
        self.name = name
        self.doctor_response_id = doctor_response_id
        self.doctor_data = doctor_data
        self.cep = cep
        self.price = price
        self.description = description

class Agenda(db.Model):
    __tablename__='agendas'

    id = db.Column(db.Integer, primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client_data = db.relationship('Client', foreign_keys=client_id)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    doctor_data = db.relationship('Doctor', foreign_keys=doctor_id)

    specialty_id = db.Column(db.Integer, db.ForeignKey('specialtys.id'))
    specialty_data = db.relationship('Specialty', foreign_keys=specialty_id)

    occupation_area_id = db.Column(db.Integer, db.ForeignKey('occupation_areas.id'))
    occupation_area_data = db.relationship('Occupation_area', foreign_keys=occupation_area_id)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_data = db.relationship('User', foreign_keys=user_id)

    consult_date = db.Column(db.DateTime)
    agenda_obs = db.Column(db.String)

    def __init__ (self,client_id,doctor_id,doctor_data,specialty_id,occupation_area_id,user_id,consult_date,agenda_obs):
        
        self.client_id = client_id
        self.doctor_id = doctor_id
        self.doctor_data = doctor_data
        self.specialty_id = specialty_id
        self.occupation_area_id = occupation_area_id
        self.user_id = user_id
        self.consult_date = consult_date
        self.agenda_obs = agenda_obs
    
    def __repr__(self):
        return '<Agenda %r>' %self.id
    

