from flask import Flask, jsonify, request
from Category.routes import category
from Configuration.routes import configuration
from Customer.routes import customer
from Instance.routes import instance
from Resource.routes import resource
import json

app = Flask(__name__)
DB = {"recursos": [], "categorias": [], "configuraciones": [], "clientes": [], "instancias": []}


@app.route('/')
def index():
    return {'msg': 'Esta es una api que funciona! Bienvenido al lobby uwu.'}


@app.route('/consultarDatos', methods=['GET'])
def consultarDatos():
    with open('DB.json') as f:
        db = json.load(f)
    return db, 200


@app.route('/reset', methods=['DELETE'])
def resetDB():
    print(DB)
    with open('DB.json', 'w') as f:
        json.dump(DB, f)
    return {'msg': 'Se reinició la base de datos exitosamente.'}


@app.route('/generarFactura', methods=['GET'])
def generarFactura():
    return jsonify({'message': 'Generar Factura'})


app.register_blueprint(category)
app.register_blueprint(configuration)
app.register_blueprint(customer)
app.register_blueprint(instance)
app.register_blueprint(resource)

if __name__ == '__main__':
    app.run(debug=True)
