import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f"Você acabou de abrir o livro '{self.titulo}' que tem {self.total_paginas} páginas no total. Você agora esta na pagina {self.pagina_atual}")
    
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range (qtd):
            if self.fim_do_livro():
                break
            time.sleep(0.3)
            self.pagina_atual += 1
            print(f"Pág{self.pagina_atual} -> ", end='')
            cont += 1
        print(f"Você avançou {cont} páginas e agora esta na página {self.pagina_atual}")
        if self.fim_do_livro():
            print(f"Você chegou ao final do livro '{self.titulo}'")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("10 coisas que eu aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)