# Classes em Python – O que é uma classe em Python
"""
- Exemplo 01: Casa
- Exemplo 02: Pessoa
- Exemplo 03: Carro

- Exemplo 04: Criar em Conjunto a Turma (Professor)
- Exemplo 04: Criar em Conjunto a Turma (PC Gamer)
"""


# Exemplo 01: Casa
class Casa:
    def __init__(self, cor, porta, garagem, cidade):
        self.cor = cor     # atributo
        self.porta = porta # atributo

minha_casa = Casa("Azul", "Madeira", "Grande", "Brusque")
print(minha_casa.cor)
print(minha_casa.porta)


# Exemplo 02: Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # atributo
        self.idade = idade    # atributo

p1 = Pessoa("Ruan", 25)
p2 = Pessoa("Maria", 30)

print(p1.nome)   # Ruan
print(p2.nome)   # Maria


# Exemplo 03: Carro
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor       # atributo 
        self.modelo = modelo # atributo

meu_carro = Carro("Preto", "Civic")
print(meu_carro.cor)      # preto
print(meu_carro.modelo)   # Civic


# ----- x ----- #

# Classes em Python – Herança, O que é a Herança de Classes em Python?

# Exemplo 01: Herança de Classe
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def ligar(self):
        print(f"{self.marca} está ligado.")

class Carro(Veiculo):
    def buzinar(self):
        print("Buzinando: BEEP BEEP!")

c = Carro("Toyota")
c.ligar()    # herdado
c.buzinar()  # próprio da classe Carro


# Exemplo 02: Usando o super()
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)  # chama __init__ de Animal
        self.cor = cor