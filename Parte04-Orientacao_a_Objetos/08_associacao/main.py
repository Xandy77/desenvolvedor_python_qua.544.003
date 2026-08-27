from models import Endereco, Pessoa

def main():
    endereco = Endereco(uf="", cidade="")
    usuario = Pessoa(nome="", endereco=endereco)

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.endereco.uf = input("Informe a UF: ").strip().upper()
    usuario.endereco.cidade = input("Informe a cidade: ").strip()

    # saida de dados
    usuario.apresentar_endereco()

if __name__ == "__main__":
    main()