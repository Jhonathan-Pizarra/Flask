from flask import Flask, request, render_template

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    #Logger para manfar informacion a la consola de la ruta que accedemos
    app.logger.info(f'Entramos al path {request.path}')
    return "Hola Mundo! - Flask Jhon"

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html') #Creamos una carpeta "templates" y ahí el .html que renderizaremos

#También podemos pasar valores de forma dinámica
@app.route('/mostrar-apellido/<apellido>', methods=['GET','POST'])
def mostrar_apellido(apellido):
    return render_template('mostrar.html', apellido=apellido)