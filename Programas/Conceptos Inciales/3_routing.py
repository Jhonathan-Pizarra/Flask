from flask import Flask, request

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    #Logger para manfar informacion a la consola de la ruta que accedemos
    app.logger.info(f'Entramos al path {request.path}')
    return "Hola Mundo! - Flask Jhon"

@app.route('/saludar')
def saludar():
    return "Hola!"

#También podemos recibir parámetos,
# los parámetos pueden ser de distintos tipos: string, int, float, path, uuid.
#STRING:
@app.route('/despedir/<nombre>')
def despedir(nombre):
    return f'Adiós! {nombre}'

#Las variables podemos trabajarlas como toda la vida, .upper(), .lower(), etc.
#INT
@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tienes {edad} años.'
#No es necesario que la path se llame igual a la función!

