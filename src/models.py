import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import DateTime


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250))
    apellido = Column(String(250))
    fecha_subscripcion = Column(DateTime)
    favoritos = Column(Integer, ForeignKey('favorito.id'))

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion = Column(Integer)
    terreno = Column(Integer)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))
    genero = Column(String(50))

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))


render_er(Base, 'diagram.png')
