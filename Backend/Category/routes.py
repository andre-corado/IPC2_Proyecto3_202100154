from flask import Blueprint, jsonify, request
from Backend.Category.model import Categoria
import Backend.DB as DB

category = Blueprint('category', __name__)


# ------------------------- Crear Categoría------------------------------

@category.route('/crearCategoria', methods=['POST'])
def crearCategoria():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'descripcion' in body and 'cargaTrabajo' in body:
            if not DB.isCategoriaatDB(str(body['id'])):
                config = Categoria(body['id'], body['nombre'], body['descripcion'], body['cargaTrabajo'])
                config.agregarADB()
                return {'msg': 'Configuración creada exitosamente.'}, 201
            else:
                return {'msg': f'El id \'{body["id"]}\' ya pertenece a una configuración.'}, 400
        else:
            return {'msg': 'Faltan campos en la petición'}, 400
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
