from BD import Base_datos

class Pollo:
    def __init__(self, id_pollo, dato_edad, raza_pollo):
        self.codigo_pollo = id_pollo
        self.edad_pollo = dato_edad
        self.raza_pollo = raza_pollo
        self.objBase_datos = Base_datos()  # Instancia de la base de datos

    # Métodos para obtener y modificar atributos
    def getCodigo_pollo(self):
        return self.codigo_pollo

    def setCodigo_pollo(self, codigo_pollo):
        self.codigo_pollo = codigo_pollo

    def getEdad_pollo(self):
        return self.edad_pollo

    def setEdad_pollo(self, edad_pollo):
        self.edad_pollo = edad_pollo

    def getRaza_pollo(self):
        return self.raza_pollo

    def setRaza_pollo(self, raza):
        self.raza_pollo = raza

    # Métodos para interactuar con la base de datos
    def guardar_pollo(self):
        self.objBase_datos.guardar_pollo(self.codigo_pollo, self.raza_pollo, self.edad_pollo)
