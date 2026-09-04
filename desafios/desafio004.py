class Livro:
    def __init__(self, titulo, total_pagina):
        self.titulo = titulo
        self.total_pagina = total_pagina
        self.pagina_atual = 0
    
    def avancar_paginas(self):
        if self.pagina_atual >= self.total_pagina:
            return f"Você ja chegou no final do livro!"
        self.pagina_atual += 1
        return f"Você esta na pagina {self.pagina_atual}"


l1 = Livro("10 coisas que aprendi", 10)
for numero_paginas in range(12):
    print(l1.avancar_paginas())