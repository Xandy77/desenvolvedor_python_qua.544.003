class Endereco:
    def __init__(self, uf, cidade):
        self._uf = uf
        self._cidade = cidade

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf):        
        self._uf = uf

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade
   
    def obter_endereco(self):
        return f"{self._cidade} - {self._uf}"


class Pessoa:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    def apresentar_endereco(self):
        print(f"\nNome: {self._nome}")
        print(f"Endereço: {self._endereco.obter_endereco()}")
        