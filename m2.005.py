print("Gerador de PA.")
print("-" * 30)
num1 = int(input("Digite o primeiro termo: "))
numx = num1
raz = int(input("Digite a razão: "))
cont_raz = 0
cont_tot = 0
print("Primeiro termo: {}" .format(num1))
print("Razão: {}" .format(raz))
print("-" * 30)
while True:
    print(numx, end=" ")
    cont_tot += 1
    cont_raz += 1
    numx += raz
    if cont_raz == 10:
        print()
        num_mais = int(input("Quanto numeros mais você quer? "))
        if num_mais == 0:
            print("-" * 30)
            print("Fim da PA. \nEsses foram os {} primeiros termos" .format(cont_tot))
            break
        else:
            cont_raz -= num_mais

