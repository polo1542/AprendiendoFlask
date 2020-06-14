from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<name>')
def index(name):
   return'<h1>Hola {}! </h1>'.format(name)
   
@app.route('/home')
def home():
   return'<h1>Hola esta es la pagina Home! </h1>'

@app.route('/json')
def json():
   return jsonify({'key':'value', 'listkey':[1,2,3]})

if __name__=='__main__':
   app.run(debug=True)

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py