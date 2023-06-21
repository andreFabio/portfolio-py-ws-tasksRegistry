from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Etiquetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fechaCreacion = db.Column(db.Date)
    fechaFinalizacion = db.Column(db.Date)
    titulo = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    tiempoConsumido = db.Column(db.Integer)
    idEtiqueta = db.Column(db.Integer, db.ForeignKey('etiquetas.id'))
    etiquetas = db.relationship('Etiquetas', backref=db.backref('tareas'))