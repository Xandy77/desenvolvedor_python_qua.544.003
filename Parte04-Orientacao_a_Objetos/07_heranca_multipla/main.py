import os

from models import Filho

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar()
    junior = Filho(
        nome= "", cpf= "", email= "", telefone= "", profissao= "",
        peso= 0.0, altura= 0.0, olhos= "", cabelo= ""
    )

    # entrada de dados
    junior.nome = input("Informe o nome: ").strip().title()
    junior.cpf = input("Informe o CPF: ").strip()
    junior.email = input("Informe o e-mail: ").strip().lower()
    junior.telefone = input("Informe o telefone: ").strip()
    junior.profissao = input("Informe a profissão: ").strip()
    junior.peso = float(input("Informe o peso em kg: ").replace(',', '.'))
    junior.altura = float(input("Informe a altura em metros: ").replace(',', '.'))
    junior.olhos = input("Informe a cor dos olhos: ").strip()
    junior.cabelo = input("Informe a cor do cabelo: ").strip()

    # saida de dados
    limpar()
    junior.exibir_dados()
    junior.mostrar_fisico()

if __name__ == "__main__":
    main()