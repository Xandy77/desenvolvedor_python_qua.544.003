# Lambda: é uma função simplificada, ou seja, pequena.
# abaixo a função somar feita em uma linha apenas
somar = lambda x, y: x+y

# função principal
def main():
    x = int(input("Informe o valor de X: "))
    y = int(input("Informe o valor de Y: "))

    print(f"O valor da soma é : {somar(x, y)}")
    

if __name__ == "__main__":
    main()