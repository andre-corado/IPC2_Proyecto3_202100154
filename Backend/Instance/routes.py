from flask import Blueprint, jsonify, request

instance = Blueprint('instance', __name__)


# ------------------------- Crear Instancia------------------------------

@instance.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    return jsonify({'message': 'Crear Instancia'})
