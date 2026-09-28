class Churrasco:

    consumo_padrao = 0.500 # consumo por pessoa
    preco_kg = 52.90 # preço do kg da carne

    def __init__(self, titulo, quantidade_pessoas):
        self.titulo = titulo
        self.quantidade_pessoas = quantidade_pessoas


    def analisar(self):
        
        self.quantidade_carne = self.quantidade_pessoas * Churrasco.consumo_padrao
        self.custo_total = self.quantidade_carne * Churrasco.preco_kg
        self.dinheiro_por_pessoa = self.custo_total / self.quantidade_pessoas
        return (
        f"Analisando {self.titulo} com {self.quantidade_pessoas} convidados\n"
        f"Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg de carne custa R${Churrasco.preco_kg:.2f}\n"
        f"Recomendo comprar {self.quantidade_carne}Kg de carne.\n"
        f"O Custo total: R${self.custo_total:.2f}\n"
        f"Cada pessoa pagará R${self.dinheiro_por_pessoa:.2f}"
    )

c1 = Churrasco("Churras dos Rapazes", 4)
print(c1.analisar())