class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    raphael = Pessoa(nome='Raphael')
    arkantus = Pessoa(raphael,nome='Arkantus')
    print(Pessoa.cumprimentar(arkantus))
    print(id(arkantus))
    print(arkantus.cumprimentar())
    print(arkantus.nome)
    print(arkantus.idade)
    for filho in arkantus.filhos:
        print(filho.nome)
    arkantus.sobrenome = 'Castro'
    del arkantus.filhos
    print(arkantus.__dict__)
    print(raphael.__dict__)
