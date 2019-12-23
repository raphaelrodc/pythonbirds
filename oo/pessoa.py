class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade = 27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    arkantus.olhos = 1
    del arkantus.olhos
    print(raphael.__dict__)
    print(arkantus.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(arkantus.olhos)
    print(raphael.olhos)
    print(id(Pessoa.olhos), id(arkantus.olhos), id(raphael.olhos))
    print(Pessoa.metodo_estatico(), arkantus.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), arkantus.nome_e_atributos_de_classe())