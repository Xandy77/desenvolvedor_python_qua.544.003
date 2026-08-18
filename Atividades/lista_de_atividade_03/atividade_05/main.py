# TODO: atividade 05
# Usando recursividade, crie um programa onde o usuário informa
# um número inteiro e o programa calcula a sequência de Fibonacci
# até o número informado.


def fibonacci(numero):
    if numero <= 1:
        return numero

    return fibonacci(numero - 1) + fibonacci(numero - 2)


# algoritmo principal

limite = int(input("Informe um número inteiro: "))

print("\nSequência de Fibonacci:")

for i in range(limite + 1):
    print(fibonacci(i), end=" ")