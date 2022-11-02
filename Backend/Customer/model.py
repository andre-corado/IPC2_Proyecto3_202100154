class Cliente:
    def __init__(self, nit, nombre, usuario, clave, direccion, correoElectronico, listaInstancias):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correoElectronico = correoElectronico
        self.listaInstancias = listaInstancias
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
