from flask import Blueprint, render_template
from ..utils import insertar_personaje, insertar_episodio, personajes_de_episodio

from app.db import db

perfil_ruta=Blueprint('perfil_ruta',__name__)
@perfil_ruta.route('/<int:page>')
@perfil_ruta.route('/')
def index(page=1):
    paginas={"inicio":1,"fin":43}
    lista_personajes=insertar_personaje(page)
    return render_template('index.html',lista=lista_personajes,paginas=paginas,page=page)

@perfil_ruta.route('/perfil/<int:id>')
def perfil(id):
    personaje=db.personajes.find_one({'id':id})
    
    return render_template('perfil.html',personaje=personaje)

@perfil_ruta.route('/perfil_ep/<int:id>')
def perfil2(id):
    personaje=db.personajes.find_one({'id':id})
    
    return render_template('perfil2.html',personaje=personaje)

@perfil_ruta.route('/capitulo/<int:id>')
def episodio(id=1):
   insertar_episodio()
   lista_personajes=personajes_de_episodio(id)
   return render_template('episodio.html',lista_personajes=lista_personajes,id_ep=id)