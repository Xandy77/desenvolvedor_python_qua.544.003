from models import Carro

def main():
    carro = Carro(modelo="", potencia=0)

    carro.modelo = input("Informe o modelo do carro: ")
    carro.potencia = int(input("Informe a potência do motor: "))
    

    print(carro.detalhes())

if __name__ == "__main__":
    main()