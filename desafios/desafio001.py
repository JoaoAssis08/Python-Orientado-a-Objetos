class Funcionario:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em video"
    
    def aprentacao(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}"
    

f1 = Funcionario("João", "Desenvolvimento", "Dev Jr")
f2 = Funcionario("Maria", "Adminstração", "Ditetora")
print(f1.aprentacao())
print(f2.aprentacao())
