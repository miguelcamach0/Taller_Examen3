class Base_datos:
    def __init__(self):
        self.lista_datos = []
        self.produccion_huevos = {}

    def guardar_pollo(self, codigo, raza, edad):
        self.lista_datos.append([codigo, raza, edad])

    def actualizar_pollo(self, codigo, nueva_raza, nueva_edad):
        for pollo in self.lista_datos:
            if pollo[0] == codigo:
                pollo[1] = nueva_raza
                pollo[2] = nueva_edad

    def eliminar_pollo(self, codigo):
        self.lista_datos = [pollo for pollo in self.lista_datos if pollo[0] != codigo]
        if codigo in self.produccion_huevos:
            del self.produccion_huevos[codigo]

    def registrar_huevos(self, codigo, semana, cantidad):
        if codigo not in self.produccion_huevos:
            self.produccion_huevos[codigo] = {}
        self.produccion_huevos[codigo][semana] = cantidad

    def obtener_produccion_total(self, codigo):
        if codigo in self.produccion_huevos:
            return sum(self.produccion_huevos[codigo].values())
        return 0

    def obtener_produccion_por_semana(self, codigo, semana):
        if codigo in self.produccion_huevos and semana in self.produccion_huevos[codigo]:
            return self.produccion_huevos[codigo][semana]
        return 0
