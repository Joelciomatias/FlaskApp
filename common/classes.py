class Funcionario_old():
    def __init__(self, nome, salario):
      self.nome = nome
      self.salario = salario
    def dados(self):
        return {'nome':self.nome,'salário':self.salario}

class Admin(Funcionario):
    def __init__(self, nome, salario):
      super().__init__(nome,salario)
    def atualizar_dados(self,nome):
        self.nome = nome
        return self.dados()

class Funcionario():
    aumento = 1.04
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def dados(self):
        return {'nome':self.nome, 'salário':self.salario}
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    @classmethod
    def definir_novo_aumento(cls,novo_aumento):
        cls.aumento = novo_aumento
    @staticmethod
    def dia_util(dia):
        if(dia.weekday() == 5 or dia.weekday() == 6):
            return False
        return True
joelcio = Funcionario('joelcio',7000)
Funcionario.definir_novo_aumento(1.05)

joelcio.aplicar_aumento()

print(joelcio.dados())
import datetime
data = datetime.date(2019,10,5)

print(Funcionario.dia_util(data))

def soma_args(*args):
    return sum(args)
def metoto_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

print(metoto_kwargs(2,'23','sd',nome='ame',idade=23))    
print(soma_args(3,4,4,4,4))
#args antes de kwargs