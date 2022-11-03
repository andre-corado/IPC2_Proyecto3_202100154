import json


class Recurso:
    def __init__(self, id, nombre, abrev, metr, tipo, valorXhora):
        self.id = str(id)
        self.nombre = str(nombre)
        self.abreviatura = str(abrev)
        self.metrica = metr
        self.tipo = str(tipo)
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