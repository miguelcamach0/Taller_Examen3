class Pollo:
    
    #metodos constructores
    def __init__(self, id_pollo, dato_edad, raza_pollo):
        #atributos de la clase (get y set)
        self.codigo_pollo = id_pollo
        self.edad_pollo = dato_edad
        self.raza_pollo = raza_pollo
        
        #llamados de otras clases
        self.objBase_datos = base_datos() # el objeto de la clase
        
        
    #metodos públicos de modificar atributos
    def getCodigo_pollo(self):
        return self.codigo_pollo
    
    def setCodigo_pollo(self, codigo_pollo):
        self.codigo_pollo = codigo_pollo
        
    def getEdad_pollo(self):
        return self.edad_pollo
    
    def setEdad_pollo(self, edad_pollo):
        self.edad_pollo = edad_pollo
        
    #Metodos para conectar base datos
    def guardar_pollo(self):
        