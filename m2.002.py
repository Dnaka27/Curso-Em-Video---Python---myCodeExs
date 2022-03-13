print("Verificando número primo")
num = int(input("Digite um número: "))
cont = 0
max = num + 1
for i in range(1, max):
    if num % i == 0:
        print("\033[33m", end="")
        cont += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(i), end="")
print("\n\033[mO número {} foi dividido {} vezes." .format(num, cont), end=" ")
if cont == 2:
    print("Por isso ele é primo.")
else:
    print("Por isso ele não é primo.")