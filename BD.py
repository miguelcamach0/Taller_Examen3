class Base_datos:
    def __init__(self):
        self.lista_datos = [
            ["P001", "Pequeña", "15 días"],
            ["P002", "Grande", "5 días"]
        ]

    def imprimir_info(self):
        for info_pollo in self.lista_datos:
            print(info_pollo)

    def agregar_pollo(self, nuevo_pollo):
        self.lista_datos.append(nuevo_pollo)

    def buscar_pollo(self, codigo):
        for pollo in self.lista_datos:
            if pollo[0] == codigo:
                return pollo
        return None

    def actualizar_pollo(self, codigo, nueva_raza, nueva_edad):
        for pollo in self.lista_datos:
            if pollo[0] == codigo:
                pollo[1] = nueva_raza
                pollo[2] = nueva_edad
                return True
        return False

    def eliminar_pollo(self, codigo):
        for i, pollo in enumerate(self.lista_datos):
            if pollo[0] == codigo:
                del self.lista_datos[i]
                return True
        return False
