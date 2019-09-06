from app import app
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app.config['SQLAlCHEMY_DATABASE_URI']= "sqlite:///databases/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    

class listaC(singleton):
    t = []
    datos = db.engine.execute('select * from users;')
    for row in datos:
        t.append(row)

lista = listaC()
Llsta1 = lista.t
l = listaC()
lis = l.t