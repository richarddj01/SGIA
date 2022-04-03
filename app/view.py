from cmath import log
from crypt import methods
from flask import render_template,request
from users_dao import datos_usuarios,insertar_usuario, users_login
from app import app

@app.route('/')
def index():
    #return render_template('login.html',users=datos_usuarios())
    return render_template('login.html')

#Despues del login, el usuario ingresa a ver las noticias
@app.route('/login',methods=['POST'])
def login():
    if request.method == "POST":
        usuario = request.form['user']
        clave = request.form['password']
        usuario_consultado = users_login(usuario,clave)
        if usuario_consultado[0][0]=='admin':
            return render_template('plantilla.html')
    return 'No se pudo acceder'

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/insertar',methods=['POST'])
def insertar():
    if request.method=="POST":
        usuario = request.form['user']
        clave = request.form['password']
        insertar_usuario(usuario,clave)
        return 'ok'
    else:
        return 'no'
    return render_template('registro.html')

@app.route('/news/<post>/')
def news(post):
    return render_template('news.html',post=post)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(port=80)