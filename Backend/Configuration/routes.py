from flask import Blueprint, jsonify, request
from Backend.Configuration.model import Configuracion
import Backend.DB as DB
configuration = Blueprint('configuration', __name__)


# ------------------------- Crear Configuración------------------------------

@configuration.route('/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'descripcion' in body:
            if 'idCategoria' in body:
                if not DB.isConfigatDB(str(body['id'])):
                    if DB.isCategoriaatDB(str(body['idCategoria'])):
                        if 'recursos' in body:
                            recursos = body['recursos']
                            for recurso in recursos:
                                if not DB.isRecursoatDB(recurso['id']):
                                    return {'msg': f'El id \'{recurso["id"]}\' no pertenece a ningún recurso.'}, 400
                            config = Configuracion(body['id'], body['idCategoria'], body['nombre'], body['descripcion'],
                                                   recursos=body['recursos'])
                        else:
                            config = Configuracion(body['id'], body['idCategoria'], body['nombre'], body['descripcion'])
                        config.agregarADB()
                        DB.addConfig(config.idCategoria, {"id": config.id})
                        return {'msg': 'Configuración creada exitosamente.'}, 201
                    else:
                        return {'msg': f'El id \'{body["idCategoria"]}\' no pertenece a ninguna categoría.'}, 400
                else:
                    return {'msg': f'El id \'{body["id"]}\' ya pertenece a una configuración.'}, 400
            else:
                return {'msg': 'Falta indicar el idCategoria.'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

