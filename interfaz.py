from pollo import Pollo

class Interfaz:
    def __init__(self):
        self.lista_pollos = []

    def mostrar_menu(self):
        while True:
            print("\n=== MENÚ DE LA GRANJA ===")
            print("1. Registrar nuevo pollo")
            print("2. Ver todos los pollos")
            print("3. Actualizar datos de un pollo")
            print("4. Eliminar un pollo")
            print("5. Registrar producción de huevos")
            print("6. Consultar producción total")
            print("7. Consultar producción por semana")
            print("8. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_pollo()
            elif opcion == "2":
                self.leer_pollos()
            elif opcion == "3":
                self.actualizar_pollo()
            elif opcion == "4":
                self.eliminar_pollo()
            elif opcion == "5":
                self.registrar_produccion()
            elif opcion == "6":
                self.consultar_produccion_total()
            elif opcion == "7":
                self.consultar_produccion_por_semana()
            elif opcion == "8":
                print("👋 Hasta luego.")
                break
            else:
                print("❌ Opción inválida.")

    def crear_pollo(self):
        codigo = input("Código del pollo: ")
        raza = input("Raza: ")
        edad = input("Edad: ")
        pollo = Pollo(codigo, edad, raza)
        pollo.guardar_pollo()
        self.lista_pollos.append(pollo)
        print("✅ Pollo registrado.")

    def leer_pollos(self):
        if not self.lista_pollos:
            print("⚠️ No hay pollos registrados.")
        else:
            for pollo in self.lista_pollos:
                print(f"Código: {pollo.getCodigo_pollo()}, Raza: {pollo.getRaza_pollo()}, Edad: {pollo.getEdad_pollo()}")

    def actualizar_pollo(self):
        codigo = input("Código del pollo a actualizar: ")
        for pollo in self.lista_pollos:
            if pollo.getCodigo_pollo() == codigo:
                nueva_raza = input("Nueva raza: ")
                nueva_edad = input("Nueva edad: ")
                pollo.setRaza_pollo(nueva_raza)
                pollo.setEdad_pollo(nueva_edad)
                pollo.objBase_datos.actualizar_pollo(codigo, nueva_raza, nueva_edad)
                print("🔁 Datos actualizados.")
                return
        print("❌ Pollo no encontrado.")

    def eliminar_pollo(self):
        codigo = input("Código del pollo a eliminar: ")
        for i, pollo in enumerate(self.lista_pollos):
            if pollo.getCodigo_pollo() == codigo:
                pollo.objBase_datos.eliminar_pollo(codigo)
                del self.lista_pollos[i]
                print("🗑️ Pollo eliminado.")
                return
        print("❌ No se encontró ese pollo.")

    def registrar_produccion(self):
        codigo = input("Código del pollo: ")
        semana = input("Semana (ej: Semana 1): ")
        cantidad = int(input("Cantidad de huevos: "))
        for pollo in self.lista_pollos:
            if pollo.getCodigo_pollo() == codigo:
                pollo.objBase_datos.registrar_huevos(codigo, semana, cantidad)
                print(" Producción registrada.")
                return
        print(" Pollo no encontrado.")

    def consultar_produccion_total(self):
        codigo = input("Código del pollo: ")
        for pollo in self.lista_pollos:
            if pollo.getCodigo_pollo() == codigo:
                total = pollo.objBase_datos.obtener_produccion_total(codigo)
                print(f" Producción total de {codigo}: {total} huevos.")
                return
        print("Código inválido.")

    def consultar_produccion_por_semana(self):
        codigo = input("Código del pollo: ")
        semana = input("Semana a consultar: ")
        for pollo in self.lista_pollos:
            if pollo.getCodigo_pollo() == codigo:
                cantidad = pollo.objBase_datos.obtener_produccion_por_semana(codigo, semana)
                print(f"En {semana}, {codigo} puso {cantidad} huevos.")
                return
        print("No se encontró ese pollo.")
