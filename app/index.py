from flask import Flask, render_template,request
from users_dao import datos_usuarios,insertar_usuario

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',users=datos_usuarios())

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