#Vamos a crear una página nueva en templates, la cual manejará el error 404
from flask import Flask, request

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    return "Hola!"

#API REST, ya no respondemos con código HTML ni Strings, sino con JSON, esto orginina servicios web
@app.route('/api/mostrar/<nombre>')
def mostar_json(nombre):
    valores = {'nombre': nombre, 'método': request.method}
    return valores

#Ejercicio, añádase el método POST
@app.route('/api/show/<apellido>', methods=['GET','POST'])
def mostrar_json2(apellido):
    valores = {'apellido': apellido, 'método': request.method}
    return valores