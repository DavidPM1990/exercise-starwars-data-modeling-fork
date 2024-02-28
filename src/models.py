import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250))
    apellido = Column(String(250))
    fecha_subscripcion = Column(DateTime, default=datetime.utcnow)  # Agregado para la fecha de suscripción

    planetas_favoritos = relationship('PlanetaFavorito', foreign_keys='PlanetaFavorito.usuario_id', cascade='all,delete')
    personajes_favoritos = relationship('PersonajeFavorito', foreign_keys='PersonajeFavorito.usuario_id', cascade='all,delete')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion = Column(Integer)  # Agregado para la población del planeta

    planetas_favoritos = relationship('PlanetaFavorito', foreign_keys='PlanetaFavorito.planeta_id', cascade='all,delete')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(50))  # Agregado para el género del personaje
    personajes_favoritos = relationship('PersonajeFavorito', foreign_keys='PersonajeFavorito.personaje_id', cascade='all,delete')

class PlanetaFavorito(Base):
    __tablename__ = 'planeta_favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    usuario = relationship('Usuario', foreign_keys=[usuario_id], cascade='all,delete')
    planeta = relationship('Planeta', foreign_keys=[planeta_id], cascade='all,delete')

class PersonajeFavorito(Base):
    __tablename__ = 'personaje_favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    usuario = relationship('Usuario', foreign_keys=[usuario_id], cascade='all,delete')
    personaje = relationship('Personaje', foreign_keys=[personaje_id], cascade='all,delete')

render_er(Base, 'diagram.png')
