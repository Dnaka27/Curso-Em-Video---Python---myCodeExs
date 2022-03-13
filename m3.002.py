print("Listagem de preços")
lista = ("lápis", 2.00, "Caderno", 8.00, "Borracha", 3.00)
print("-" * 40)
print(f'{"Lista de preços":^40}')
print("-" * 40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end="")
    else:
        print(f"R$:{lista[i]:>7.2f}")