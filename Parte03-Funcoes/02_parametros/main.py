# função com parâmetros
def boas_vindas(nome): # essa parte repete após a variável nome, conforme vemos abaixo
    print(f"Seja bem vindo, {nome}! 😜😊😊")

# algoritmo principal
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)