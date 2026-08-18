# TODO: atividade 04
# utilizando o conceito de módulo, crie um módulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - calcula a potência de um número informado pelo usuário elevado...
# - a outro número informado pelo usuário.
# - calcula a raiz quadrada de um número informado pelo usuário.
# - calcula o volume de um recipiente paralelepídico.
# - calcula o volume de um recipiente cilíndrico.
# - Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Retorna a base elevada ao expoente.
def calcular_potencia(base, expoente):
    return base ** expoente

# Retorna a raiz quadrada de um número (valores positivos).
def calcular_raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Não existe raiz quadrada real de número negativo."
    return math.sqrt(numero)

# Calcula o volume de um paralelepípedo (C x L x A).
def volume_paralelepipedo(comprimento, largura, altura):
    return comprimento*largura*altura

# Calcula o volume de um cilindro (pi * r² * h).
def volume_cilindro(raio, altura):
    return math.pi * (raio ** 2) * altura