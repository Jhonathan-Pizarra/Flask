from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configuracion de la bdd
USER_DB = 'postgres'
PASS_DB = '123123'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicialización de db sqlalchemy y hacer operaciones hacia l abdd
db = SQLAlchemy(app)

#configurar flask-migrate
#Esto permite realizar las migraciones y que se pueda crear el mapeo la siguiente clase de pyrhon (Clase Persona) hacia la bdd
migrate = Migrate()
migrate.init_app(app, db)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))


    def __str__(self):
        return (
            f'Id: {self.id},'
            f'Nombre: {self.nombre},'
            f'Apellido: {self.apellido},'
            f'Email: {self.email}'
        )


#Proceso de migracion (Tenido ya hecho el script)
# flask db init (Crea la carpeta migrations)
# flask db migrate (Crea el archivo que representa la migración de la tabla hacia la bdd)
# flask db updgrade (Se guardan los cambios y aparecen en la bdd de postgres)

#Si por alguna razón fallara este proceso, o si tuvieramos que hacer una modificación sobre este modelo_
# flask db stamp head (Verificar que todo esté actualizado al momento)
# flask db migrate (Para migrar cualquier cambio actual o adicional)
# flask db  upgrade (Se guardan las actualizaciones sobre la base de datos a partir de nuestro modelo)

