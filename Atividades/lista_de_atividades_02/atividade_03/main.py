import json
import os

alunos = [] # a lista não pode ficar dentro while true para não reiniciar a lista

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:

    print("1 - Cadastrar aluno")
    print("2 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:

        case "1":
            # criando dicionário
            aluno = {}
            notas = [0,0,0]

            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i] = float(input(f"Informe a {i+1}ª nota: ").replace(",","."))
            aluno['notas'] = notas
            aluno['média'] = sum(notas)/len(notas)
            aluno['resultado'] = "aprovado" if aluno ['média'] >= 7 else "reprovado"
            alunos.append(aluno)

            with open(f"arquivo.json", "w", encoding="utf-8") as f:
                json.dump(alunos, f)
                print("Dados do aluno gravados com sucesso!")
                continue

        case "2":
            break

        case _:
            print("Opção inválida.")
            continue
           
        # TODO: atividade 03
        # Crie um programa que receba o nome de um aluno e 3 notas.
        # O programa deve calcular a média do aluno e informar se
        # o aluno está aprovado (média mínima = 7) ou reprovado.
        # O programa deve gravar esses dados em um JSON.
        # Ao final, o usuário deverá escolher se deseja inserir as
        # notas de outro aluno, que deverão ser gravadas no mesmo
        # arquivo JSON.