from flask import Blueprint, jsonify, request

category = Blueprint('category', __name__)


# ------------------------- Crear Categoría------------------------------

@category.route('/crearCategoria', methods=['POST'])
def crearCategoria():
    return jsonify({'message': 'Crear Categoría'})
