from Estrella import Estrella
class Galaxia(Estrella):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.estrellas = []
        
    def __str__(self):
        return f"Galaxia en coordenadas: ({self.x}, {self.y}, {self.z})"
    
    def __mane__(self):
        return f"Galaxia: {self.x}, {self.y}, {self.z}"
    
    def agregar_estrella(self, estrella):
        self.estrellas.append(estrella)