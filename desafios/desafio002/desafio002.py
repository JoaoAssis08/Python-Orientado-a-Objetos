class Produto:

    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def etiqueta(self):
        return f"O produto é o {self.nome} e o preço dele é R$ {self.preço:,.2f}"

p1 = Produto("Celular", 800)
print(p1.etiqueta())