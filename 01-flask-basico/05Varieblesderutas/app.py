from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home', methods=['POST', 'GET'], defaults={'name':'Amigo'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
   return'<h1>Hola {}! esta es la pagina Home! </h1>'.format(name) 

@app.route('/json')
def json():
   return jsonify({'key':'value', 'listkey':[1,2,3]})

if __name__=='__main__':
   app.run(debug=True)

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py