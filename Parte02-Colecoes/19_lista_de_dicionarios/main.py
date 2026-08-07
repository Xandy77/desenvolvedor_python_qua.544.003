usuarios = [
    {
        'nome': "Valdomiro",
        'idade': 39,
        'email': "domirops@yahoo.com.br"
    },

    {
        'nome': "Verinha",
        'idade': 37,
        'email': "veralucia@gmail.com"
    },
    {
        'nome': "Tchuco",
        'idade': 4,
        'email': "tchucotchuco@gmail.com"
    }
]

# percorre a lista de dicionários
for usuario in usuarios:
    for chave, valor in usuario.items(): # separa a variável chave do valor é o sentido da vírgula
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")