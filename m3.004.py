print("Criando lista ordenada")
print("-" * 30)
tam = int(input("Digite o tamanho da lista: "))
lista = []
for i in range(0, tam):
    num = int(input("Digite um número: "))    
    if i == 0 or num >= lista[-1]:
        lista.append(num)
        print("Número adicionado")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Número adicionado a posição {pos}")
                break
            pos += 1
print("-" * 30)
print(f"Os valores digitados em ordem foram{lista}")
