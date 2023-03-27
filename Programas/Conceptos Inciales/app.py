from flask import Flask

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    return "Hola Mundo! - Flask Jp"

#Correr co el comando:
# flask --app (archivo) run

#Establecer en modo de desarrollo
#Windows:
# set FLASK_APP=(archivo a ejecutar en el servidor).py Ejemplo: set FLASK_APP=app.py
# set FLASK_ENV=development
# correr el comando: flask --app (archivo) run --debug

#Mac o Linux: export FLASK_APP=app.py


#Documentacion oficial: https://flask.palletsprojects.com/en/2.2.x/
