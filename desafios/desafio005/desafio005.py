class Gamer:

    def __init__(self, nome, nick, jogos_favoritos):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = jogos_favoritos
    
    def mostrar_ficha(self):
        return f"O nome do jogador(a) é {self.nome} e o nickname dele(a) é {self.nick} e os jogos faviritos dele(a) é {self.jogos_favoritos}"