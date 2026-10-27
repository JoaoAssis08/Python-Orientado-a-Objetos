from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados = 0):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados = 4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return 2 * (3.14 * self.raio)

    def area(self):
        return 3.14 * (5**2)

