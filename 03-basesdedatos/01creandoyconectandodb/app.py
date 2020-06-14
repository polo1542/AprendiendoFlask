from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3
#La variable g es global y nos ayuda para realizar la conexion
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Esunsecreto!'

def conexion_db():
   '''
   Esta funcion sirve para realizar la conexion con una base de datos realizada anteriormente con sqlite3, es un poco mas sencillo que con SQLAlchemy
   '''
   sql = sqlite3.connect('/Users/paulvazkz/Documents/flask-projects/03-basesdedatos/01creandoyconectandodb/data.db')
   sql.row_factory = sqlite3.Row
   return sql

def obtener_db():
   if not hasattr(g, 'sqlite3') :
      g.sqlite_db = conexion_db()
   return g.sqlite_db

@app.teardown_appcontext
def cerrar_db(error):
   if hasattr(g, 'sqlite_db'):
      g.sqlite_db.close()

@app.route('/')
def index():
   session.pop('name', None)
   return '<h1>Hola, mundo</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name':'Amigo'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
   session['name'] = name 
   #Con lo siguiente realizamos una consulta para mostrar todos los registros
   db = obtener_db()
   cur = db.execute('select id, name, location from users')
   results = cur.fetchall()

   return render_template('home.html', name=name, display=True,\
       mylist=['uno', 'dos', 'tres', 'cuatro '], listofdictionaries = [{'nombre':'Pablo'}, {'nombre':'Zoe'}], results=results)

@app.route('/json')
def json():
   if 'name'in session :
      name = session['name']
   else:
      name='No esta en sesion'
   return jsonify({'key':'value', 'listkey':[1,2,3], 'name': name})

@app.route('/query')
def query ():
   name = request.args.get('name')
   location = request.args.get('location')
   return '<h1>Hola {}. Y tu eres de {}. Esta es la pagina Query</h1>'.format(name, location)
#Ahora insertaremos datos desde nuestro formulariocy que cy
@app.route('/theform', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
      return render_template('form.html')
    else:
       name = request.form['name']
       location = request.form['location']
       #insertar registro
       db = obtener_db()
       db.execute('insert into users (name, location) values (?,?)', [name, location])
       db.commit()
       #return '<h1>Hola {}. Y tu eres de {}. Haz llenado el Formulario bien</h1>'.format(name, location)
       return redirect(url_for('home', name=name, location=location))
#Probar con PostMan 
@app.route('/processjson', methods=['POST'])
def processjson():
   data = request.get_json()
   name = data['name']
   location = data['location']
   randomlist = data['randomlist']
   return jsonify({'result': 'Success!', 'name':name,' location':location,'randomkeylist': randomlist[1] })

@app.route('/verresultados')
def verresultados ():
   db = obtener_db()
   cur = db.execute('select id, name, location from users')
   results = cur.fetchall()
   #esta sentencia hace que veamos un dato por uno
   return '<h1>El Id es {}. El nombre es {}. Y es de {}.</h1>'.format(results[2]['id'], results[2]['name'], results[2]['location'])

if __name__=='__main__':
   app.run()

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py