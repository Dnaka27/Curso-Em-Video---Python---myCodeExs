print("Matrizes 2")
print("-" * 30)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para {i}, {c}: "))
print("-" * 30)
for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{matriz[x][y]:^5}]", end=" ")
        if matriz[x][y] % 2 == 0:
            spar += matriz[x][y]
    print()
print("-" * 30)
print(f"A soma dos valores pares é {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}.")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior elemento da segunda linha é {mai}")