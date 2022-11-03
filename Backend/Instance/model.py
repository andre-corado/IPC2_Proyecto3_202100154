import json


class Instancia:
    def __init__(self, id, idConfig, idCliente, nombre, fechaInicio, estado, fechaFinal=None):
        self.id = str(id)
        self.idConfiguracion = str(idConfig)
        self.idCliente = str(idCliente)
        self.nombre = str(nombre)
        self.fechaInicio = fechaInicio
        self.estado = str(estado)
        self.fechaFinal = fechaFinal

    def json(self):
        return {
            "id": self.id,
            "idConfiguracion": self.idConfiguracion,
            "idCliente": self.idCliente,
            "nombre": self.nombre,
            "fechaInicio": self.fechaInicio,
            "estado": self.estado,
            "fechaFinal": self.fechaFinal
        }

    def agregarADB(self):
        with open('DB.json') as f:
            db = json.load(f)
        instancias = db['instancias']
        instancias.append(self.json())
        with open('DB.json', 'w') as f:
            json.dump(db, f, indent=2)
