import random
import json
import Backend.DB as DB


class Cliente:
    def __init__(self, nit, nombre, direccion, correoElectronico):
        self.nit = str(nit)
        self.nombre = str(nombre)
        self.usuario = self.nit
        self.clave = self.nombre + str(random.randrange(1, 999))
        self.direccion = str(direccion)
        self.correoElectronico = str(correoElectronico)
        self.instancias = []

    def json(self):
        return {
            "nit": self.nit,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "clave": self.clave,
            "direccion": self.direccion,
            "correoElectronico": self.correoElectronico,
            "instancias": self.instancias
        }

    def agregarADB(self):
        DB.agregaraDB(self.json(), 'clientes')
