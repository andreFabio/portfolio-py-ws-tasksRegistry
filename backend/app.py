from flask import Flask,render_template, request, redirect, url_for
from models import Tareas,db

#from flask_sqlalchemy import SQLAlchemy,db

    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://roote:roote@localhost/Agenda'  # Reemplaza con tu propia configuración de conexión
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/tarea/nueva', methods=['GET', 'POST'])
def nueva_tarea():
    if request.method == 'POST':
        # Obtén los datos del formulario y crea una nueva tarea en la base de datos
        tarea = Tarea(
            fecha_creacion=request.form['fecha_creacion'],
            fecha_finalizacion=request.form['fecha_finalizacion'],
            titulo=request.form['titulo'],
            descripcion=request.form['descripcion'],
            tiempo_consumido=request.form['tiempo_consumido'],
            id_etiqueta=request.form['id_etiqueta']
        )
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        # Renderiza el formulario para crear una nueva tarea
        return render_template('nueva_tarea.html')

# Agrega las vistas para editar, eliminar y ver detalles de una tarea según tus necesidades