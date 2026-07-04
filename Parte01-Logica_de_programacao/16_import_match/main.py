# importação da biblioteca
import math

# tratamento de exceção
try:
    while True:
        # usúario informa valor do raio 
        r = float(input("Inorme o valor do raio: ").replace(",","."))

        # calcula a área do circulo
        area = math.pi*r**2

        # imprime na tela a área do circulo
        print(f"Área do circulo: {area:.2f} m².")

        # usuário informa se deseja continuar ou não
        print("1 - Calcular área de outro círculo.")
        print("2 - Sair do programa.")

        opcao = input("Informe sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção Inválida.")
                continue
        

except Exception as e:
    print(f"Não foi possível calcular. {e}.")