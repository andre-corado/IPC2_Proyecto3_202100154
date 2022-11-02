import json
from Backend.Configuration.model import Configuracion


class Categoria:
    def __init__(self, id, nombre, descripcion, cargaTrabajo, listaConfiguraciones):
        self.id = id
        self.nombre = nombre
        self.descripcion =descripcion
        self.cargaTrabajo = cargaTrabajo
        self.listaConfiguraciones = listaConfiguraciones
        self.configuraciones = []
        for config in listaConfiguraciones:
            conf = Configuracion(config['id'], config['nombre'], config['descripcion'], config['recursos'])
            self.configuraciones.append(conf.json())

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "cargaTrabajo": self.cargaTrabajo,
            "configuraciones": self.configuraciones
        }