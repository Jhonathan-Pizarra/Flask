from flask import Flask, session, render_template, request, url_for, redirect

app = Flask(__name__)

# Asignar la llave secreta de forma segura
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.secret_key = 'MyKey'

#Procesar desdel el navegador
@app.route('/')
def inicio():
    if 'username' in session:
        return f'Sesión Iniciada! {session["username"]}'
    return "No ha iniciado sesión"

#LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        #Agregar usuario a la sesión
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

#LOGOUT
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))