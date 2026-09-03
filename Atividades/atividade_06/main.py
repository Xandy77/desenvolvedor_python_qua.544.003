from modulo import Pessoa, Conta, limpar


# ============================================
# FUNÇÃO PRINCIPAL
# ============================================

def main():

    # ------------------------------------------
    # Criando o titular
    # ------------------------------------------

    titular = Pessoa(
        nome="Valdomiro Pereira dos Santos",
        cpf="000.000.000-00"
    )

    # ------------------------------------------
    # Criando a conta
    # ------------------------------------------

    conta = Conta(
        titular=titular,
        agencia="0001",
        n_conta="12345-6",
        saldo=0.0
    )

    # ------------------------------------------
    # MENU
    # ------------------------------------------

    while True:

        limpar()

        print("======================================")
        print("          SISTEMA BANCÁRIO")
        print("======================================")
        print("1 - Consultar dados da conta")
        print("2 - Gerar extrato")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Sair")
        print("======================================")

        opcao = input("Informe a opção desejada: ").strip()

        # --------------------------------------
        # CONSULTAR DADOS
        # --------------------------------------

        if opcao == "1":

            limpar()

            conta.consultar_dados()

        # --------------------------------------
        # GERAR EXTRATO
        # --------------------------------------

        elif opcao == "2":

            limpar()

            conta.gerar_extrato()

        # --------------------------------------
        # DEPOSITAR
        # --------------------------------------

        elif opcao == "3":

            limpar()

            try:

                valor = float(
                    input("Informe o valor do depósito: R$ ")
                )

                conta.depositar(valor)

            except ValueError:

                print("\nDigite um valor numérico válido.")

        # --------------------------------------
        # SACAR
        # --------------------------------------

        elif opcao == "4":

            limpar()

            try:

                valor = float(
                    input("Informe o valor do saque: R$ ")
                )

                conta.sacar(valor)

            except ValueError:

                print("\nDigite um valor numérico válido.")

        # --------------------------------------
        # SAIR
        # --------------------------------------

        elif opcao == "5":

            limpar()

            print("Programa encerrado.")

            break

        # --------------------------------------
        # OPÇÃO INVÁLIDA
        # --------------------------------------

        else:

            print("\nOpção inválida.")

        input("\nPressione ENTER para continuar...")


# ============================================
# PROTEÇÃO DO PROGRAMA
# ============================================

if __name__ == "__main__":
    main()
