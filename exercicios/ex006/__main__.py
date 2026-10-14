#from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("João", 18, "ADS", "A3008")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1)

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1)

    f1 = Funcionario("Célio", 51, "Desenvolvedor", "TI")
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1)

if __name__ == "__main__":
    main()