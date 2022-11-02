import json


class Instancia:
    def __init__(self, id, idConfig, nombre, fechaInicio, estado, fechaFinal):
        self.id = id
        self.idConfiguracion = idConfig
        self.nombre = nombre
        self.fechaInicio = fechaInicio
        self.estado = estado
        self.fechaFinal = fechaFinal

    def json(self):
        return {
            "id": self.id,
            "idConfiguracion": self.idConfiguracion,
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
