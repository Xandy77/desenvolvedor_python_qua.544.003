# dicionário
usuario = {
    'nome': "Valdomiro",
    'idade': 39,
    'e-mail': "domirops@yahoo.com.br",
    'cpf': "123.456.789-10"
}

# adiciona a chave telefone ao dicionário
usuario['telefone'] = input(f"Informe o telefone de {usuario.get('nome')}: ").strip()

# exibe o dicionário
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")