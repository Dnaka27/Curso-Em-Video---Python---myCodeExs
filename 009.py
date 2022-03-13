from random import randint
computador = randint(0, 5)
print("---" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("---" * 20)
while True:
    num = int(input("Em que número pensei? "))
    if num == computador:
        print("Parabéns, você acertou")
        break
    else:
        print("Você errou. Tente novamente")