import json
import os

ARQUIVO_JSON = "alunos_notas.json"

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# Verifica se o arquivo JSON existe
if os.path.exists(ARQUIVO_JSON):

    arquivo = open(ARQUIVO_JSON, "r", encoding="utf-8")
    alunos = json.load(arquivo)
    arquivo.close()

else:
    alunos = []


while True:

    print("1 - Cadastrar aluno")
    print("2 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()

    match opcao:

        case "1":

            # Solicita o nome do aluno
            nome = input("\nInforme o nome do aluno: ").strip().title()

            # Cria uma lista para armazenar as notas
            notas = []

            # Solicita as 3 notas
            for i in range(1, 4):

                nota = float(
                    input(f"Informe a {i}ª nota do aluno: ")
                    .replace(",", ".")
                )

                # Verifica se a nota está entre 0 e 10
                while nota < 0 or nota > 10:

                    print("A nota deve estar entre 0 e 10.")

                    nota = float(
                        input(f"Informe novamente a {i}ª nota: ")
                        .replace(",", ".")
                    )

                # Adiciona a nota na lista
                notas.append(nota)

            # Calcula a média
            media = sum(notas) / len(notas)

            # Verifica a situação
            if media >= 7:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            # Mostra o resultado
            print(f"Aluno: {nome}")
            print(f"Notas: {notas}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")
           

            # Cria o dicionário do aluno
            aluno = {
                "nome": nome,
                "notas": notas,
                "media": round(media, 2),
                "situacao": situacao
            }

            # Adiciona o aluno à lista
            alunos.append(aluno)

           

        case "2":

            print("\nPrograma encerrado!")
            break

        case _:

            print("\nOpção inválida!")
            print("Escolha 1 para cadastrar ou 2 para sair.")