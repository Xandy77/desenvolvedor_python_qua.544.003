# TODO: atividade 04
# utilizando o conceito de módulo, crie um módulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - calcula a potência de um número informado pelo usuário elevado...
# - a outro número informado pelo usuário.
# - calcula a raiz quadrada de um número informado pelo usuário.
# - calcula o volume de um recipiente paralelepídico.
# - calcula o volume de um recipiente cilíndrico.
# - Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

from modulo import limpar,potencia,raiz,volume_cubico,volume_cilindro

def main():
    limpar()
    while True:
        print("1 - Calcular potência")
        print("2 - Calcular raíz")
        print("3 - Calcular volume cúbico")
        print("4 - Calcular volume cilíndrico")
        print("5 - Sair")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                x = int(input("Informe um número inteiro: "))
                y = int(input("Informe a potência: "))
                print(f"{x} elevado a {y} = {potencia(x, y)}")
                continue
            case "2":
                x = int(input("Informe um número inteiro: "))
                print(f"Raíz quadrada de {x} = {raiz(x)}")
                continue
            case "3":
                b = int(input("Informe o valor da base: "))
                l = int(input("Informe o valor da largura: "))
                h = int(input("Informe o valor da altura: "))
                print(f"Volume cúbico é {volume_cubico(b, l, h)}")
                continue
            case "4":
                r = int(input("Informe o valor do raio: "))
                h = int(input("Informe o valor da altura: "))
                print(f"Volume do cilindro é {volume_cilindro(b, h)}")
                continue
            case "5":
                break
            case _:
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()


'''
import modulo 

modulo.limpar()

def exibir_menu():
    print("\n===== CALCULADORA =====")
    print(" 1 - Calcular Potência.")
    print(" 2 - Calcular Raiz Quadrada.")
    print(" 3 - Calcular Volume do Paralelepípedo.")
    print(" 4 - Calcular Volume do Cilindro.")
    print(" 5 - Sair do programa.")
    
   

def main():
    modulo.limpar()
    while True:
        
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            b = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = modulo.calcular_potencia(b, expoente)
            print(f"Resultado: {b} elevado a {expoente} = {resultado:.2f}")

        elif opcao == "2":
            n = float(input("Digite o número para extrair a raiz: "))
            resultado = modulo.calcular_raiz_quadrada(n)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"A raiz quadrada de {n} é {resultado:.2f}")

        elif opcao == "3":
            comp = float(input("Digite o comprimento: "))
            larg = float(input("Digite a largura: "))
            alt = float(input("Digite a altura: "))
            vol = modulo.volume_paralelepipedo(comp, larg, alt)
            print(f"O volume do recipiente paralelepípedo é: {vol:.2f}")

        elif opcao == "4":
            r = float(input("Digite o raio da base do cilindro: "))
            alt = float(input("Digite a altura do cilindro: "))
            vol = modulo.volume_cilindro(r, alt)
            print(f"O volume do recipiente cilíndrico é: {vol:.2f}")

        elif opcao == "5":
            print("\nSaindo do programa... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            

if __name__ == "__main__":
    main() 

'''
