from dataclasses import dataclass

@dataclass
class Pessoa:
    telefone: str
    email: str

    # instanciar o método
    def __str__(self):
        return f"Telefone: {self.telefone}\nEmail: {self.email}"

    def __del__(self):
        print(f"Objetos {self} foi morto com sucesso! 🥲")

@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str
    profissao: str
    idade: int
    salario: float

    # instanciar o método
    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nProfissão: {self.profissao}\nIdade: {len(self)}anos\nSálario: R$ {float(self):.2f}\n{super().__str__()}"

    def __len__(self):
        return self.idade

    def __float__(self):
        return self.salario

@dataclass
class PessoaJuridica(Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str
    valor_mercado: float

    def __str__(self):
        return f"Nome da empresa: {self.nome_fantasia}\nRazão Social: {self.razao_social}\nCNPJ: {self.cnpj}\nValor de mercado: R$ {float(self):.2f}\n{super(),self.__str__()}"