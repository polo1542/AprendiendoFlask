from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
   return'<h1>Hola {}! </h1>'.format(name)

if __name__=='__main__':
   app.run(debug=True)

#para ejeuctarlo ya es mas facil y solo necesitamos poner en consola
#python app.py