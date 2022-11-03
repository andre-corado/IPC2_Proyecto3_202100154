import json
from Backend.Configuration.model import Configuracion
import Backend.DB


class Categoria:
    def __init__(self, id, nombre, descripcion, cargaTrabajo):
        self.id = str(id)
        self.nombre = str(nombre)
        self.descripcion = str(descripcion)
        self.cargaTrabajo = str(cargaTrabajo)
        self.configuraciones = []

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "cargaTrabajo": self.cargaTrabajo,
            "configuraciones": self.configuraciones
        }

    def agregarADB(self):
        Backend.DB.agregaraDB(self.json(), 'categorias')
