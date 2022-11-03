from flask import Blueprint, jsonify, request
from Backend.Instance.model import Instancia
import Backend.DB as DB
instance = Blueprint('instance', __name__)


# ------------------------- Crear Instancia------------------------------

@instance.route('/crearInstancia', methods=['POST'])
def crearInstancia():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'idConfiguracion' in body and 'fechaInicio' in body and 'estado' in body:
            if 'idCliente' in body:
                if not DB.isInstanciaatDB(str(body['id'])):
                    if DB.isConfigatDB(str(body['idConfiguracion'])):
                        if DB.isClienteatDB(str(body['idCliente'])):
                            if body['estado'] == 'Vigente' or body['estado'] == 'Cancelada':
                                if body['estado'] == 'Cancelada':
                                    if not 'fechaFinal' in body:
                                        return {'msg': 'Falta el parámetro fechaFinal, ya que se encuentra en estado '
                                                       'Cancelada.'}, 400
                                    instancia = Instancia(body['id'], body['idConfiguracion'], body['idCliente'],
                                                          body['nombre'], body['fechaInicio'], body['estado'],
                                                          fechaFinal=body['fechaFinal'])
                                    instancia.agregarADB()
                                    DB.addInstancia(instancia.idCliente, {'id': instancia.id})
                                    return {'msg': 'Instancia creada exitosamente.'}, 201
                                else:
                                    instancia = Instancia(body['id'], body['idConfiguracion'], body['idCliente'],
                                                          body['nombre'], body['fechaInicio'], body['estado'])
                                    instancia.agregarADB()
                                    DB.addInstancia(instancia.idCliente, {'id': instancia.id})
                                    return {'msg': 'Instancia creada exitosamente.'}, 201
                            else:
                                return {'msg': 'El parámetro estado debe de ser Vigente o Cancelada.'}, 400
                        else:
                            return {'msg': f'El nit \'{body["idCliente"]}\' no pertenece a ningún cliente.'}, 400
                    else:
                        return {'msg': f'El id \'{body["idConfiguracion"]}\' no pertenece a ninguna configuración.'}, 400
                else:
                    return {'msg': f'El id \'{body["id"]}\' ya pertenece a una instancia.'}, 400
            else:
                return {'msg': 'Falta el parámetro idCliente.'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
