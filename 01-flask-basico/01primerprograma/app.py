from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
   return'<h1>Hola {}! </h1>'.format(name)

#para correrlo se ejecutan los sguiente comandos
# set FLASK_APP=app.py
# flask run