# Cada objeto possui caracterisiticas diferentes mas são da mesma Classe 
# Método Construtor: é uma ação que minha classe para aquele objeto seja construido
# Os métodps sempre vão receber no minimo um argumento
# classe Pessoa
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, altura):  # Self é o método, o que vem após são os argumentos(atributos) 
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    # método
    def exibir_dados(self): # Se o meu método não recebe parametros então ele irá receber Self
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos.")
        print(f"E-mail: {self.email}")
        print(f"Altura: {self.altura} metros.")

    # Criando a função main()
def main():
    # Instanciar a classe(criar um objeto)
    usuario = Pessoa(nome="", idade=0, email="", altura=0.0)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o seu email: ").strip().lower()
    usuario.altura = float(input("Informe a altura em metros: ").replace(",","."))

    usuario.exibir_dados()


if __name__ == "__main__":
    main()