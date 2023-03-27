from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    return "FLASK"

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('inicio')) #pasamos como parametro el nombre de la función o método

#Si queremos redireccionar a una path que espera un argumento, lo hacemos así:
#1) Tenemos la función a redireccionar
@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html')

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tienes {edad} años.'

#2) definimos la función redireccionar2
@app.route('/redireccionar2')
def redireccionar_nombre():
    return redirect(url_for('mostrar_nombre', nombre='Jhon')) #pasamos como parametro el nombre de la función o método
