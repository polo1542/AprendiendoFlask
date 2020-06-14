from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/home', methods=['POST', 'GET'], defaults={'name':'Amigo'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
   return'<h1>Hola {}! esta es la pagina Home! </h1>'.format(name) 

@app.route('/json')
def json():
   return jsonify({'key':'value', 'listkey':[1,2,3]})

@app.route('/query')
def query ():
   name = request.args.get('name')
   location = request.args.get('location')
   return '<h1>Hola {}. Y tu eres de {}. Esta es la pagina Query</h1>'.format(name, location)

@app.route('/theform')
def form():
   return '''<form method="POST" action="/process">
               <input type="text" name="name">
               <input type="text" name="location">
               <input type="submit" value="Enviar">
             </form>'''

@app.route('/process', methods=['POST', 'GET'])
def process():
   name = request.form['name']
   location = request.form['location']
   return '<h1>Hola {}. Y tu eres de {}. Haz llenado el Formulario bien</h1>'.format(name, location)


#Probar con PostMan 
@app.route('/processjson', methods=['POST'])
def processjson():

   data = request.get_json()

   name = data['name']
   location = data['location']

   randomlist = data['randomlist']

   return jsonify({'result': 'Success!', 'name':name,' location':location,'randomkeylist': randomlist[1] })

if __name__=='__main__':
   app.run(debug=True)

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py