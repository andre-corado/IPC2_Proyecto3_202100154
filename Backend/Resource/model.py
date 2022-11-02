import json


class Recurso:
    def __init__(self, id, nombre, abrev, metr, tipo, valorXhora):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abrev
        self.metrica = metr
        self.tipo = tipo
        self.valorXHora = valorXhora

    def json(self):
        return {
        "id" : self.id, "nombre" : self.nombre, "abreviatura" : self.abreviatura, "metrica" : self.metrica,
        "tipo" : self.tipo, "valorXHora" : self.valorXHora
        }

    def agregarADB(self):
        with open('DB.json') as f:
            db = json.load(f)
        recursos = db['recursos']
        recursos.append(self.json())
        with open('DB.json', 'w') as f:
            json.dump(db, f, indent=2)