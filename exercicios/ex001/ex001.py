# Declaração de Classe
class Gafanhoto:
    def __init__(self): #Metodo Contrutor
        # Atributos de Instancia
        self.nome = ""
        self.idade = 0

    # Métodos de instancia
    def aniverio(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 12
g1.aniverio()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "João"
g2.idade = 18
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())