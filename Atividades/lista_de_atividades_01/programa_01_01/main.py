# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário, e informe na tela o seu IMC o seu diagnóstico com base no valor do IMC.
"""
# NOTE: imc = peso/(altura**2)

# importando biblioteca os
import os

# limpa tela do terminal
os.system("cls" if os.name == "nt" else "clear")

nome = input("Digite seu nome: ").strip()
peso = float(input("Digite seu peso (kg): ").replace(",","."))
altura = float(input("Digite sua altura (m): ").replace(",","."))

imc = peso / (altura ** 2)

print(f"\nNome: {nome}")
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Diagnóstico: Abaixo do peso")
elif imc < 25:
    print("Diagnóstico: Peso normal")
elif imc < 30:
    print("Diagnóstico: Sobrepeso")
elif imc < 35:
    print("Diagnóstico: Obesidade Grau I")
elif imc < 40:
    print("Diagnóstico: Obesidade Grau II")
else:
    print("Diagnóstico: Obesidade Grau III")