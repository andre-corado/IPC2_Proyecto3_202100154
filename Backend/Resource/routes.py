from flask import Blueprint, jsonify, request
from Backend.Resource.model import Recurso
resource = Blueprint('resource', __name__)


# ------------------------- Crear Recurso------------------------------

@resource.route('/crearRecurso', methods=['POST'])
def crearRecurso():
    return {'msg' : 'Crear Recurso'}

