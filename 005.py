nome = input("Digite seu nome completo: ").strip()
print("Características do nome:")
print("Seu nome em maiúsculas é: {}" .format(nome.upper()))
print("Seu nome em minúsculas é: {}" .format(nome.lower()))
print("Seu nome tem {} letras" . format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras" .format(nome.find(" "))) # = Mostra onde esta o primeiro espaço (posição 3) assim conta as letras do primeiro nome