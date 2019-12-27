class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    raphael = Mutante(nome='Raphael')
    arkantus = Homem(raphael,nome='Arkantus')
    print(Pessoa.cumprimentar(arkantus))
    print(id(arkantus))
    print(arkantus.cumprimentar())
    print(arkantus.nome)
    print(arkantus.idade)
    for filho in arkantus.filhos:
        print(filho.nome)
    arkantus.sobrenome = 'Castro'
    del arkantus.filhos
    arkantus.olhos = 1
    del arkantus.olhos
    print(raphael.__dict__)
    print(arkantus.__dict__)
    print(Pessoa.olhos)
    print(arkantus.olhos)
    print(raphael.olhos)
    print(id(Pessoa.olhos), id(arkantus.olhos), id(raphael.olhos))
    print(Pessoa.metodo_estatico(), arkantus.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), arkantus.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(raphael, Pessoa))
    print(isinstance(raphael, Homem))
    print(raphael.olhos)
    print(arkantus.cumprimentar())
    print(raphael.cumprimentar())