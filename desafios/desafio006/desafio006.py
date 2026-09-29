from rich import print

class Caneta:
    def __init__ (self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, mensagem):
        if self.tampada:
            print(f":prohibited: A {self.cor} caneta[/] está tampada!")
        else:
            print(f"{self.cor}{mensagem}[/]", end='')

    def quebrar_linha(self, quantidade = 1):
        print("\n" * quantidade, end='' )

    def tampar_caneta(self):
        self.tampada = True

    def destampar_caneta(self):
        self.tampada = False

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")
c1.destampar_caneta()
c2.destampar_caneta()

c1.escrever("Olá, Mundo!")
c2.escrever("Funciona!")
c2.quebrar_linha(2)
c3.escrever("Deu certo!")
c3.quebrar_linha(5)
c1.escrever("Sera que Rola?")