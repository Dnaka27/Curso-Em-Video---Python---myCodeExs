print("Lista dentro de outra")
print("-" * 30)
tam = int(input("Quantas pessoas irá cadastrar? "))
dados = []
pessoa = []
grupo = []
for i in range(0, tam):
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    dados.append(nome)
    dados.append(peso)

    grupo.append(dados[-2:])
print(grupo)
