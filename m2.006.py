print("Sequência de fibonacci")
num = int(input("Digite quantos termos você quer mostrar? "))
cont = 2
print("-" * 30)
t1 = 0
t2 = 1
print("{} -> {} -> " .format(t1, t2), end="")
while cont < num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print("{} -> " .format(t3), end="")
    cont += 1
print("Fim")