import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     addresses = relationship('Address', backref='person', lazy=True)

# class Address(Model):
#     id = Column(Integer, primary_key=True)
#     email = Column(String(120), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'),
#         nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(50))
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(50),nullable=False)
    phone = Column(Integer) 
    like = relationship('Like',backref='user',lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(String(50))
    gravity = Column(String(50))
    rotation_period = Column(Integer)
    orbital_period= Column(Integer)
    diameter = Column(Integer)
    surface_water = Column(Integer)
    character = relationship('Character', backref='planet',lazy=True)
    like = relationship('Like', backref='planet',lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew= Column(Integer)
    passenger = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(50))
    vehicle_class = Column(String(50))
    like = relationship('Like', backref='vehicle',lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(Integer)
    birth_year = Column(Integer)
    gender = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    like = relationship('Like', backref='character',lazy=True)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user_id = Column(Integer,ForeignKey('user.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
