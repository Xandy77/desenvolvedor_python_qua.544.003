import os

from models import Pedido


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    
    # Primeiro lemos o texto, trocamos a vírgula por ponto, e depois convertemos para float
    v1_texto = input("Informe o primeiro valor: ").replace(",", ".")
    v2_texto = input("Informe o segundo valor: ").replace(",", ".")
    
    valor1 = float(v1_texto)
    valor2 = float(v2_texto)

    # Instancia a classe usando os nomes corretos esperados pelo __init__
    pedido = Pedido(valor1=valor1, valor2=valor2)

    limpar()
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    operador = input("Escolha a operação desejada: ").strip()
     
    limpar()
    print(f"Resultado: {pedido.calcular_total(operador=operador)}")

if __name__ == "__main__":
    main()

