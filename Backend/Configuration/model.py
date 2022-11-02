class Configuracion:
    def __init__(self, id, nombre, descripcion, recursosConfiguracion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.recursosConfiguracion = recursosConfiguracion
        self.recursos = []
        for rec in recursosConfiguracion:
            self.recursos.append({"id": rec['id'], 'cantidad': rec['cantidadRecurso']})

    def json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "recursos": self.recursos
        }
