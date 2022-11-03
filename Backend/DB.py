import json


def isIDofTypeatDB(id, type, idNombre='id'):
    with open('DB.json') as f:
        db = json.load(f)
    grupoDB = db[type]
    for dato in grupoDB:
        if dato[idNombre] == id:
            return True
    return False

def agregaraDB(objetoJSON, tipo):
    with open('DB.json') as f:
        db = json.load(f)
    grupoDB = db[tipo]
    grupoDB.append(objetoJSON)
    with open('DB.json', 'w') as f:
        json.dump(db, f, indent=20)

def getObjectofTypeatDB(id, type, idNombre='id'):
    with open('DB.json') as f:
        db = json.load(f)
    grupoDB = db[type]
    for dato in grupoDB:
        if dato[idNombre] == id:
            return dato

def addObjectToList(id, objetoJSON, tipo, lista, idNombre = 'id'):
    with open('DB.json') as f:
        db = json.load(f)
    tipoDB = db[tipo]
    for dato in tipoDB:
        if dato[idNombre] == id:
            listaDB = dato[lista]
            listaDB.append(objetoJSON)
    with open('DB.json', 'w') as f:
        json.dump(db, f, indent=20)

def isRecursoatDB(id):
    return isIDofTypeatDB(id, 'recursos')

def isConfigatDB(id):
    return isIDofTypeatDB(id, 'configuraciones')

def isCategoriaatDB(id):
    return isIDofTypeatDB(id, 'categorias')

def isClienteatDB(id):
    return isIDofTypeatDB(id, 'clientes', idNombre='nit')

def isInstanciaatDB(id):
    return isIDofTypeatDB(id, 'instancias')

def isEmailatDB(email):
    return isIDofTypeatDB(email, 'clientes', idNombre='correoElectronico')

def addConfig(idCategoria, config):
    addObjectToList(idCategoria, config, 'categorias', 'configuraciones')

def addRecurso(idConfig, recurso):
    addObjectToList(idConfig, recurso, 'configuraciones', 'recursos')

def addInstancia(idCliente, instancia):
    addObjectToList(idCliente, instancia, 'clientes', 'instancias', idNombre='nit')
