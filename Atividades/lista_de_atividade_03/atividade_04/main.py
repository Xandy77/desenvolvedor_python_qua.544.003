# TODO: atividade 04
# utilizando o conceito de módulo, crie um módulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - calcula a potência de um número informado pelo usuário elevado...
# - a outro número informado pelo usuário.
# - calcula a raiz quadrada de um número informado pelo usuário.
# - calcula o volume de um recipiente paralelepídico.
# - calcula o volume de um recipiente cilíndrico.
# - Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

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
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = modulo.calcular_potencia(base, expoente)
            print(f"Resultado: {base} elevado a {expoente} = {resultado:.2f}")

        elif opcao == "2":
            num = float(input("Digite o número para extrair a raiz: "))
            resultado = modulo.calcular_raiz_quadrada(num)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"A raiz quadrada de {num} é {resultado:.2f}")

        elif opcao == "3":
            comp = float(input("Digite o comprimento: "))
            larg = float(input("Digite a largura: "))
            alt = float(input("Digite a altura: "))
            vol = modulo.volume_paralelepipedo(comp, larg, alt)
            print(f"O volume do recipiente paralelepípedo é: {vol:.2f}")

        elif opcao == "4":
            raio = float(input("Digite o raio da base do cilindro: "))
            alt = float(input("Digite a altura do cilindro: "))
            vol = modulo.volume_cilindro(raio, alt)
            print(f"O volume do recipiente cilíndrico é: {vol:.2f}")

        elif opcao == "5":
            print("\nSaindo do programa... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            

if __name__ == "__main__":
    main() 
