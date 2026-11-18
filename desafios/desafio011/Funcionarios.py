from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        vezes_salario = self.salario / self.sal_min
        return (
            f"O salário de {self.nome} é de R${self.salario:.2f} e corresponde a {vezes_salario:.1f} salarios minimos"
        )

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        desconto_inss = self.sal_bruto * self.inss / 100
        self.salario = self.sal_bruto - desconto_inss


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_sal(self):
        desconto_inss = self.sal_bruto * self.inss / 100
        self.salario = self.sal_bruto - desconto_inss
