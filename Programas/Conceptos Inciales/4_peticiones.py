from flask import Flask, request

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    #Logger para manfar informacion a la consola de la ruta que accedemos
    app.logger.info(f'Entramos al path {request.path}')
    return "Hola Mundo! - Flask Jhon"

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return f'Hola {nombre}'