
# ============================================
# modulo.py
# ============================================

import os
from dataclasses import dataclass
from abc import ABC, abstractmethod


# ============================================
# FUNÇÃO PARA LIMPAR A TELA
# ============================================

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# ============================================
# INTERFACE IConta
# ============================================

class IConta(ABC):

    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def gerar_extrato(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


# ============================================
# CLASSE Pessoa
# ============================================

@dataclass
class Pessoa:

    nome: str
    cpf: str

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"


# ============================================
# CLASSE Conta
# ============================================

@dataclass
class Conta(IConta):

    titular: Pessoa
    agencia: str
    n_conta: str
    saldo: float = 0.0

    # ------------------------------------------
    # Consultar dados
    # ------------------------------------------

    def consultar_dados(self):

        print("\n========== DADOS DA CONTA ==========")

        print(self.titular)
        print(f"Agência: {self.agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    # ------------------------------------------
    # Gerar extrato
    # ------------------------------------------

    def gerar_extrato(self):

        print("\n========== EXTRATO ==========")

        print(f"Titular: {self.titular.nome}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.n_conta}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    # ------------------------------------------
    # Depositar
    # ------------------------------------------

    def depositar(self, valor):

        if valor <= 0:

            print("\nO valor do depósito deve ser maior que zero.")

            return self.saldo

        self.saldo += valor

        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

        return self.saldo

    # ------------------------------------------
    # Sacar
    # ------------------------------------------

    def sacar(self, valor):

        if valor <= 0:

            print("\nO valor do saque deve ser maior que zero.")

            return self.saldo

        if valor > self.saldo:

            print("\nSaldo insuficiente!")
            print(f"Saldo disponível: R$ {self.saldo:.2f}")

            return self.saldo

        self.saldo -= valor

        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

        return self.saldo