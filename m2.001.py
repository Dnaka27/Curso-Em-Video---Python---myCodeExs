print("Cálculo de IMC")
peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = float(peso / (altura ** 2))
print("O seu IMC é de {}" . format(imc))
if imc < 18.5:
    print("Seu peso está abaixo do ideal")
if imc > 18.5 and imc < 25:
    print("Seu peso é o ideal")
if imc >= 25 and imc < 30:
    print("Você está em sobrepeso")
if imc >= 30 and imc < 40:
    print("Você está obeso")
if imc >= 40:
    print("Você está em obesidade mórbida")