# dicionário
usuario = {
    'nome': "Valdomiro",
    'idade': 39,
    'e-mail': "domirops@yahoo.com.br",
    'cpf': "123.456.789-10"
}

# exibe os dados do dicionário
# forma 1
print("\nForma 1:")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"E-mail: {usuario['e-mail']}")
print(f"CPF: {usuario['cpf']}")

# forma 2
print("\nForma 2:")
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"E-mail: {usuario.get('e-mail')}")
print(f"CPF: {usuario.get('cpf')}")

# forma 3
print("Forma 3:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

