nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "João",
    "Maria",
    "José",
    "Esmeralda"
]

# usuário o nome que deseja deletar 
nome = input("Informe o nome que deseja deletar: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    # apaga item da lista
    del(nomes[indice])

    # exibe a nova lista sem o item deletado
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")