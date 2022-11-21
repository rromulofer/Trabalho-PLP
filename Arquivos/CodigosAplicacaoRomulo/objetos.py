# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 28/10/22
# Ciência da Computação - UENF
# Disciplina: PLP

# Definindo a Classe pessoa
class Pessoa:
    # Construtor
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Definindo o metodo dizer_ola()
    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
              f'anos e minha altura é {self.altura}m.')

    # Definindo o metodo cozinhar()
    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um(a): {receita}')

    # Definindo o metodo andar()
    def andar(self, distancia: float):
        print(f'Saí para andar. Volto quando completar {distancia} metros')


# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome='Romulo', idade=22, altura=1.77)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar('Sopa')
pessoa.andar(1200)
