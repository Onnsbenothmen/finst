from . import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    funds = db.relationship('Funds', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.firstName} {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "created_at": self.created_at,
        }

class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    userId = db.Column(db.Integer, db.ForeignKey("Users.id"))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user = db.relationship('Users', back_populates='funds')

    def serialize(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "created_at": self.created_at,
        }

class Instance(db.Model):
    __tablename__ = "instances"
    id = db.Column(db.Integer, primary_key=True)
    president_email = db.Column(db.String(100), nullable=False)
    council_name = db.Column(db.String(100), nullable=False)
    ville = db.Column(db.String(100), nullable=False)  # Ajout du champ ville
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "president_email": self.president_email,
            "council_name": self.council_name,
            "ville": self.ville,  # Incluez le champ ville dans la méthode serialize
            "active": self.active,
            "created_at": self.created_at,
        }
