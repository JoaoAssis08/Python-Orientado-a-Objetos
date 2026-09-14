# Anotações:
#Consumo por pessoa: 400g
#preço da carne: R$ 82,40/Kg


class Churrasco:

    def __init__(self, titulo, quantidade_pessoas):
        self.titulo = titulo
        self.quantidade_pessoas = quantidade_pessoas


    def analisar(self):
        
        self.quantidade_carne = self.quantidade_pessoas * 0.4
        self.custo_total = self.quantidade_carne * 82.40
        self.dinheiro_por_pessoa = self.custo_total / self.quantidade_pessoas
        return (
        f"Analisando {self.titulo} com {self.quantidade_pessoas} convidados\n"
        f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n"
        f"Recomendo comprar {self.quantidade_carne}Kg de carne.\n"
        f"O Custo total: R${self.custo_total:.2f}\n"
        f"Cada pessoa pagará R${self.dinheiro_por_pessoa:.2f}"
    )

c1 = Churrasco("Churras dos Amigos", 100)
print(c1.analisar())