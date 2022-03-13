print("Pares e ímpares de uma lista")
print("-" * 30)
i = 1
lista = [[], []]
tam = int(input("Quantos números serão digitados? "))
for i in range(1, tam + 1):
    num = int(input(f"Digite o {i}° número: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print("-" * 30)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares foram: {lista[0]}")
print(f"Os valores ímpares foram: {lista[1]}")