from flask import Blueprint, jsonify, request
from Backend.Resource.model import Recurso
import Backend.DB as DB

resource = Blueprint('resource', __name__)


# ------------------------- Crear Recurso------------------------------

@resource.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'abreviatura' in body and 'metrica' in body and 'tipo' in body \
                and 'valorXHora' in body:
            if not DB.isRecursoatDB(str(body['id'])):
                if isinstance(body['metrica'], int):
                    if body['metrica'] > 0:
                        if body['tipo'] == 'Hardware' or body['tipo'] == 'Software':
                            try:
                                body['valorXHora'] = float(body['valorXHora'])
                                if body['valorXHora'] >= 0:
                                    recurso = Recurso(body['id'], body['nombre'], body['abreviatura'], body['metrica'],
                                                      body['tipo'],
                                                      body['valorXHora'])
                                    recurso.agregarADB()
                                    return {'msg': 'Recurso creado exitosamente.'}, 201
                                else:
                                    return {'msg': 'El parámetro de valorXHora debe de ser mayor o igual a 0.'}, 400
                            except:
                                return {'msg': 'El parámetro de valorXHora debe de ser de tipo numérico.'}, 400
                        else:
                            return {'msg': 'El parámetro tipo debe de ser Hardware o Software.'}, 400
                    else:
                        return {'msg': 'El parámetro de métrica debe de ser mayor a 0.'}, 400
                else:
                    return {'msg': 'El parámetro de métrica debe de ser de tipo entero.'}, 400
            else:
                return {'msg': f'El id: \'{body["id"]}\' ya pertenece a otro recurso.'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
