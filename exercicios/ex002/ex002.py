# Declaração de Classe
class Gafanhoto:
    def __init__(self, nome = "vazio", idade = 0): #Metodo Construtor
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    # Métodos de instancia
    def aniverio(self):
        self.idade += 1

    def __str__(self):#Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniverio()
print(g1)
print(g1.__dict__)#Atributo
print(g1.__getstate__())#Metodo
