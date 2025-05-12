from pollo import Pollo

class Interfaz:
    def __init__(self):
        self.lista_pollos = []

    def crear_pollo(self):
        codigo = input("Ingrese código del pollo: ")
        raza = input("Ingrese raza del pollo: ")
        edad = input("Ingrese edad del pollo: ")

        pollo = Pollo(codigo, edad, raza)
        pollo.guardar_pollo()
        self.lista_pollos.append(pollo)
        print("Pollo registrado con éxito.")

    def leer_pollos(self):
        if not self.lista_pollos:
            print("No hay registros de pollos.")
        else:
            print("Lista de pollos:")
            for pollo in self.lista_pollos:
                print(f"Código: {pollo.getCodigo_pollo()}, Raza: {pollo.getRaza_pollo()}, Edad: {pollo.getEdad_pollo()}")

    def actualizar_pollo(self):
        codigo = input("Ingrese el código del pollo a actualizar: ")
        for pollo in self.lista_pollos:
            if pollo.getCodigo_pollo() == codigo:
                nueva_raza = input("Nueva raza: ")
                nueva_edad = input("Nueva edad: ")
                pollo.setRaza_pollo(nueva_raza)
                pollo.setEdad_pollo(nueva_edad)
                pollo.objBase_datos.actualizar_pollo(codigo, nueva_raza, nueva_edad)
                print("Pollo actualizado.")
                return
        print("Pollo no encontrado.")

    def eliminar_pollo(self):
        codigo = input("Ingrese el código del pollo a eliminar: ")
        for i, pollo in enumerate(self.lista_pollos):
            if pollo.getCodigo_pollo() == codigo:
                pollo.objBase_datos.eliminar_pollo(codigo)
                del self.lista_pollos[i]
                print("Pollo eliminado.")
                return
        print("Pollo no encontrado.")
