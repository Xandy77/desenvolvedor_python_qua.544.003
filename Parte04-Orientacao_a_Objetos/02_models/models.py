# Models: é o arquivo aonde se deve incluir as classes
class Pessoa:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome 
        self.idade = idade 
        self.email = email
        self.telefone = telefone

    # método
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, e tenho {self.idade} anos."
    
    def cumprimentar(self, nome):
        return f"Prazer em te conhecer, {nome}, meu e-mail é {self.email} e mau telefone é {self.telefone}."