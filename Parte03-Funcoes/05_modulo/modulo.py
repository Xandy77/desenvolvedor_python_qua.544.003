# Módulo: É o arquivo que irá guardar uns arquivos como se fosse uma bilbioteca
import os

# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def equacao_primeiro_grau(a, b):
    # a*x+b = 0
    return -b/a
