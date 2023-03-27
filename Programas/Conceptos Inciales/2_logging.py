from flask import Flask, request

app = Flask(__name__)

#Procesar desdel el navegador
@app.route("/")
def inicio():
    #app.run(debug=True)
    app.logger.debug('Mensaje desde debug')
    app.logger.info('Mensaje desde info')
    app.logger.warning('Mensaje desde warning')
    app.logger.error('Mensaje desde error')
    #Logger para manfar informacion a la consola de la ruta que accedemos
    app.logger.info(f'Entramos al path {request.path}')
    return "Hola Mundo! - Flask Jhon"

#Si corremos desde develpment, (flask --app 2_logging run --debug) todos los logger aparecerán
#Si corremos desde produccion, (flask --app 2_logging run) solo aparecerán los warnings y los errors
