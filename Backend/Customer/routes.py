from flask import Blueprint, jsonify, request

customer = Blueprint('customer', __name__)


# ------------------------- Crear Cliente------------------------------

@customer.route('/crearCliente', methods=['POST'])
def crearCliente():
    return jsonify({'message': 'Crear Cliente'})
