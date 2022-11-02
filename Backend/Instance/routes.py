from flask import Blueprint, jsonify, request
from Backend.Instance.model import Instancia

instance = Blueprint('instance', __name__)


# ------------------------- Crear Instancia------------------------------

@instance.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'idConfiguracion' in body and 'fechaInicio' in body and 'estado' in body \
                and 'fechaFinal' in body:
            instancia = Instancia(body['id'], body['idConfiguracion'], body['nombre'], body['fechaInicio'], body['estado'],
                                body['fechaFinal'])
            instancia.agregarADB()
            return {'msg': 'Instancia creada exitosamente.'}, 201
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
