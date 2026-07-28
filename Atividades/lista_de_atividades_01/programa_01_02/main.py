# TODO: atividade 02
"""
Crie um programa que receba uma vez o nome e a idade do usuário, e em seguida mostre os filmes em cartaz em 5 salas de cinema:
- A Volta dos Que Não Foram (livre)
- A Roda Quadrada (12 anos)
- As Tranças do Rei Careca (14 anos)
- Poeira em Alto Mar (16 anos)
- A Vingança do Frango Assado (18 anos)
O usuário irá escolher a sala onde o filme desejado está passando. Caso o usuário não tenha idade, o programa impede sua entrada e re-exibe a lista para que o mesmo possa escolher outro filme. Caso o usuário tenha a idade mínima, o programa grava em arquivo o bilhete do filme e encerra o programa.
"""

# Dados do usuário
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# Lista de filmes
filmes = {
    1: ("A Volta dos Que Não Foram", 0),
    2: ("A Roda Quadrada", 12),
    3: ("As Tranças do Rei Careca", 14),
    4: ("Poeira em Alto Mar", 16),
    5: ("A Vingança do Frango Assado", 18)
}

while True:
    print("\n===== FILMES EM CARTAZ =====")
    print("Sala 1 - A Volta dos Que Não Foram (Livre)")
    print("Sala 2 - A Roda Quadrada (12 anos)")
    print("Sala 3 - As Tranças do Rei Careca (14 anos)")
    print("Sala 4 - Poeira em Alto Mar (16 anos)")
    print("Sala 5 - A Vingança do Frango Assado (18 anos)")

    try:
        sala = int(input("\nEscolha a sala (1 a 5): "))

        if sala not in filmes:
            print("Sala inválida! Tente novamente.")
            continue

        filme, idade_minima = filmes[sala]

        if idade >= idade_minima:
            print(f"\nEntrada autorizada! Bom filme, {nome}!")

            # Grava o bilhete em arquivo
            with open("bilhete.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("===== BILHETE DE CINEMA =====\n")
                arquivo.write(f"Nome : {nome}\n")
                arquivo.write(f"Idade: {idade}\n")
                arquivo.write(f"Sala : {sala}\n")
                arquivo.write(f"Filme: {filme}\n")
                arquivo.write("=============================\n")

            print("Bilhete gravado com sucesso no arquivo 'bilhete.txt'.")
            break

        else:
            print(f"\nAcesso negado! O filme '{filme}' é permitido apenas para maiores de {idade_minima} anos.")
            print("Escolha outro filme.")

    except ValueError:
        print("Digite apenas números para a sala.")