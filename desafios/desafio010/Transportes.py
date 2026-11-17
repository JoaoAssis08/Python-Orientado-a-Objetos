from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        
    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        return(self.distancia * self.fator)


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):

        if self.distancia < 50:
            return f"A distancia minima para entrega de caminhão é de 50Km"
        else:
            return (self.distancia * self.fator)

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia > 10:
            return f"A distacia maxima para entrega de drone é 10Km"
        else:
            return (self.distancia * self.fator)
