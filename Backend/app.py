from flask import Flask, jsonify, request
from Category.routes import category
from Configuration.routes import configuration
from Customer.routes import customer
from Instance.routes import instance
from Resource.routes import resource
import json

app = Flask(__name__)

@app.route('/')
def index():
    return {'msg': 'Esta es una api que funciona! Bienvenido al lobby uwu.'}

@app.route('/consultarDatos', methods=['GET'])
def consultarDatos():
    return jsonify({'msg' : 'Consultar Datos'})


@app.route('/generarFactura', methods=['GET'])
def generarFactura():
    return jsonify({'message':'Generar Factura'})

app.register_blueprint(category)
app.register_blueprint(configuration)
app.register_blueprint(customer)
app.register_blueprint(instance)
app.register_blueprint(resource)

if __name__ == '__main__':
    app.run(debug=True)

