import json

import Backend.DB


class Configuracion:
    def __init__(self, id, idCategoria, nombre, descripcion, recursos=None):
        self.id = str(id)
        self.idCategoria = str(idCategoria)
        self.nombre = str(nombre)
        self.descripcion = str(descripcion)
        if recursos is None:
            self.recursos = []
        else:
            self.recursos = recursos

    def json(self):
        return {
            "id": self.id,
            "idCategoria": self.idCategoria,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "recursos": self.recursos
        }

    def agregarADB(self):
        Backend.DB.agregaraDB(self.json(), 'configuraciones')
