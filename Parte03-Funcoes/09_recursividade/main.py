# recursividade: quando tem algo ou alguma coisa que chama ela mesma, dentro da função ela executa ela mesma.
def fatorial(n):
    return 1 if n == 1 else  n*fatorial(n-1)

def main():
    n = int(input("Informe um número inteiro: "))
    print(f"Fatorial de {n}! é {fatorial(n)}.")

if __name__ == "__main__":
    main()