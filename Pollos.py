class Pollo:
    def __init__(self, id_pollo, edad_pollo, raza_pollo):
        self.codigo_pollo = id_pollo
        self.edad_pollo = edad_pollo
        self.raza_pollo = raza_pollo

    # Métodos Get y Set
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

    def setRaza_pollo(self, raza_pollo):
        self.raza_pollo = raza_pollo
