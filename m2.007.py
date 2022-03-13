print("Caixa eletrônico")
print("-" * 30)
valor = int(input("Qaual o valor você deseja sacar? "))
total = valor
nota = 50
totnotas = 0
while True:
    if total >= nota:
        total -= nota
        totnotas += 1
    else:
        if totnotas > 0:
            print(f"Total de {totnotas} notas de {nota} reais")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        elif nota == 2:
            nota = 1
        totnotas = 0
        if total == 0:
            break
print("-" * 30)
print("Fim da operação.")