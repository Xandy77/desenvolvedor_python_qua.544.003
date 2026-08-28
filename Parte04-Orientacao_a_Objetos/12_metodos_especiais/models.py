class Pessoa:
    # metodo construtor é "__init__"
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Obrigatorio implementar o método __str__ para que a classe seja representada como string
    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e minha altura é {self.altura:.2f}m."

    def __len__(self):
        return self.idade

    def __float__(self):
        return self.altura

    def __del__(self):
        print(f"Objeto {self} foi destruido com sucesso!!!🤣")