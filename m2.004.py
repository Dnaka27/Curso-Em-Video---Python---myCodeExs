print("Validando números")
num = int(input("Digite um número de 0 a 10: "))
while True:
    if num < 0 or num > 10:
        print("Número inválido. Digite novamente: ", end="")
        num = int(input(""))
    else:
        print("Número validado")
        break
