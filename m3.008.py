print("Matrizes")
print("-" * 30)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Digite um valor para {i}, {c}: "))
print("-" * 30)
for x in range(0, 3):
    for y in range(0, 3):
        print(f"[{matriz[x][y]:^5}]", end=" ")
    print()
