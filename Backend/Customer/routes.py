from flask import Blueprint, jsonify, request
from Backend.Customer.model import Cliente
import Backend.DB as DB
customer = Blueprint('customer', __name__)


# ------------------------- Crear Cliente------------------------------

@customer.route('/crearCliente', methods=['POST'])
def crearCliente():
    body = request.get_json()
    try:
        if 'nit' in body and 'nombre' in body and 'direccion' in body and 'correoElectronico' in body:
            if not DB.isClienteatDB(str(body['nit'])):
                if not DB.isEmailatDB(str(body['correoElectronico'])):
                    cliente = Cliente(body['nit'], body['nombre'], body['direccion'], body['correoElectronico'])
                    cliente.agregarADB()
                    return {'msg': 'Cliente creado exitosamente. Sus credenciales son las siguientes:',
                            'credenciales': {'usuario': cliente.usuario, 'clave': cliente.clave}}, 201
                else:
                    return {'msg': f'El email \'{body["correoElectronico"]}\' ya pertenece a un cliente.'}, 400
            else:
                return {'msg': f'El nit \'{body["nit"]}\' ya pertenece a un cliente.'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

