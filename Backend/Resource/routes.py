from flask import Blueprint, jsonify, request
from Backend.Resource.model import Recurso
resource = Blueprint('resource', __name__)


# ------------------------- Crear Recurso------------------------------

@resource.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'abreviatura' in body and 'metrica' in body and 'tipo' in body\
                and 'valorXHora' in body:
            recurso = Recurso(body['id'], body['nombre'], body['abreviatura'], body['metrica'], body['tipo'],
                              body['valorXHora'])
            recurso.agregarADB()
            return {'msg' : 'Recurso creado exitosamente.'}, 201
        else:
            return {'msg' : 'Faltan campos en la petición'}, 400
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

