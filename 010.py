# Multa de R$: 4,00 por cada km/h a mais
vel = int(input("Digite a velocidade do carro: "))
if vel > 80:
    print("Você foi multado.")
    print("Multa: R$:{},00" .format((vel - 80) * 4))
else:
    print("Você não foi multado.")