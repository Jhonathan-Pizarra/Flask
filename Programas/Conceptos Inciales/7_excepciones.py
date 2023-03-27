#Vamos a crear una página nueva en templates, la cual manejará el error 404
from flask import Flask, abort, render_template

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    return "Hola!"

@app.route("/salir")
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html', error=error), 404) #Podemos adjuntar el error al que nos referimos al final, pero también otros valores
