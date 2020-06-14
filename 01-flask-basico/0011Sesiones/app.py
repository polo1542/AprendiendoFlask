from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)
'''
Aqui en la configuracion hay que checar las opciones
que nos da la documentacion oficial de Flask
'''
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Esunsecreto!'

@app.route('/')
def index():
   session.pop('name', None)
   #.pop elimina la sesion
   return '<h1>Hola, mundo</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name':'Amigo'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
   session['name'] = name 
   return'<h1>Hola {}! esta es la pagina Home! </h1>'.format(name) 

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

@app.route('/theform', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
      return '''<form method="POST" action="/theform">
                  <input type="text" name="name">
                  <input type="text" name="location">
                  <input type="submit" value="Enviar">
               </form>'''
    else:
       name = request.form['name']
       location = request.form['location']

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

if __name__=='__main__':
   app.run()

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py