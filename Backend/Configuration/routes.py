from flask import Blueprint, jsonify, request

configuration = Blueprint('configuration', __name__)


# ------------------------- Crear Configuración------------------------------

@configuration.route('/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    return jsonify({'message': 'Crear Configuración'})
