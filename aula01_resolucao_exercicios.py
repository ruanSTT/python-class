# Exercicios 01: Classes em Python – O que é uma Classe em Python

"""
Exercio 1:
Crie uma classe chamada Livro que tenha apenas um atributo titulo. Depois, instancie dois livros com títulos diferentes e imprima o título de cada um.
"""

# Resultado esperado:
# Livro 1: A Menina que Roubava Livros
# Livro 2: 1984

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

livro1 = Livro("A Menina que Roubava Livros")
livro2 = Livro("1984")

print("Livro 1:", livro1.titulo)
print("Livro 2:", livro2.titulo)

"""
Exercício 2:
Crie uma classe chamada Carro com nenhum atributo ou método. Depois, imprima o tipo (type) da instância criada e comprove que ela é da classe Carro.
"""

# Resultado esperado:
# <class '__main__.Carro'>

class Carro:
    pass  # classe vazia

meu_carro = Carro()
print(type(meu_carro))  # <class '__main__.Carro'>


# --- x ---
# Exercicios 02: Classes em Python – Atributos, como iniciar atributos de uma Classe

"""
Exercicio 1:
Crie uma classe chamada Pessoa com os atributos nome e idade. No construtor (__init__), inicialize esses atributos. 
Instancie um objeto e imprima os valores.
"""

# Resultado esperado:
# Nome: João
# Idade: 25

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 25)

print("Nome:", p1.nome)
print("Idade:", p1.idade)

"""
Exercício 2:
Adicione um atributo chamado profissao à classe Pessoa. 
Inicialize via parâmetro opcional no __init__ com valor padrão 'Desempregado'.
"""

# Dica: Use profissao="Desempregado" no __init__

class Pessoa:
    def __init__(self, nome, idade, profissao="Desempregado"):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

p1 = Pessoa("João", 25)
p2 = Pessoa("Ana", 30, "Engenheira")

print(p1.nome, "-", p1.profissao)  # João - Desempregado
print(p2.nome, "-", p2.profissao)  # Ana - Engenheira


# --- x ---
# Exercicios 03: Classes em Python – O que é um Objeto em Python?

"""
Exercício 1:
Com base na classe Pessoa, instancie três objetos diferentes com valores únicos e imprima os dados de cada um.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Lucas", 20)
p2 = Pessoa("Bruna", 28)
p3 = Pessoa("Carlos", 33)

print(p1.nome, "-", p1.idade)
print(p2.nome, "-", p2.idade)
print(p3.nome, "-", p3.idade)

"""
Exercício 2:
Explique com suas próprias palavras, no comentário do código, qual a diferença entre a classe e os objetos instanciados dela.SS
"""

# Coloque a sua explicação aqui:
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# A classe Pessoa é como um molde (fôrma).
# Quando instanciamos p1 = Pessoa("Maria"), estamos criando um "objeto real".
# Objetos são instâncias de uma classe: entidades reais que vivem no programa.

p1 = Pessoa("Maria")
print(p1.nome)

# --- x ---
# Exercicios 04: Classes em Python – Métodos, O que são Métodos e Funções em Python?

"""
Exercício 1:
Crie uma classe Calculadora com dois atributos a e b, e um método soma() que retorna a soma dos dois.
"""

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

calc = Calculadora(5, 3)
print("Soma:", calc.soma())  # 8

"""
Exercício 2:
Crie uma função fora da classe que receba dois números e os multiplique. Depois, crie um método com o mesmo propósito dentro da classe. Mostre como a chamada é diferente.
"""

# Comparação esperada:
# resultado = multiplicar(2, 3)  # função
# resultado = calc.multiplicar()  # método

# Função fora da classe
def multiplicar(a, b):
    return a * b

print("Função:", multiplicar(2, 3))  # 6

# Método dentro da classe
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplicar(self):
        return self.a * self.b

calc = Calculadora(2, 3)
print("Método:", calc.multiplicar())  # 6


# --- x ---
# Exercicios 05: Classes em Python – Herança, O que é a Herança de Classes em Python?

"""
Exercício 1:
Crie uma classe Animal com um método falar() que imprime "Emitindo som...". Depois, crie uma classe Cachorro que herda de Animal e sobrescreva o método falar() com "Au Au!".
"""

# Teste:
# cachorro = Cachorro()
# cachorro.falar()  # Au Au!

class Animal:
    def falar(self):
        print("Emitindo som...")

class Cachorro(Animal):
    def falar(self):
        print("Au Au!")

c = Cachorro()
c.falar()  # Au Au!

"""
Exercício 2:
Crie uma classe Funcionario com atributos nome e salario, e uma classe Gerente que herda de Funcionario e adiciona um atributo departamento.

Use super() para herdar corretamente os atributos do pai.
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)  # chama o __init__ da superclasse
        self.departamento = departamento

g = Gerente("Fernanda", 9000, "TI")
print("Nome:", g.nome)
print("Salário:", g.salario)
print("Departamento:", g.departamento)