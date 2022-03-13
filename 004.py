# C U R S O   E M   V  I  D  E  O     P  Y  T  H  O  N
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
#frase[9:13] - "Seleciona os elementos de 9 até 12(13 - 1)"
#frase[9:21] - "Seleciona os elementos de 9 até 20(20 - 1)"
#frase[9:21:2] - "Seleciona os elementos de 9 até 20 de dois em dois"
#frase[:5] - frase[0:5]
#frase[15:] - frase[15:fim]
#frase[15::3] - "frase[15:fim] indo de 3 em 3"
#len(frase) - Tamanho em número inteiro da frase 
#frase.count("o") - Conta quantos "o"
#frase.count("o, 0, 13") - Conta quantos "o" de 0 a 12(13 - 1)
#frase.find("deo") - Indica a posicao que comeca parte selecionada
#frase.find("android") - "Quando nao encontra a parte retorna -1"
#"Curso" in frase - "Verifica a parte e retorna true ou false"
#frase.replace("Python","Android") - Substitui o primeiro pelo segundo
#frase.upper() - Coloca em maiúsculas
#frase.lower() - Coloca em minúsculas
#frase.capitalize() - Coloca todas em minúsculas e a primeira em maiúscula
#frase.title() - Coloca todas em minúsculas e a primeira de cada palavra em maiúscula
#frase.strip() - Remove os espaços inúteis
#frase.rstrip() - Remove os espaços inúteis da direita
#frase.lstrip() - Remove os espaços inúteis da esquerda
#frase.split() - Divide a frase em listas de stringes
#"-".join(frase) - Une a string com "-" no lugar dos espaços
string = "Hello, world"
divis = string.split()
print(divis[1] [0]) # = Isso irá selecionar a primeira letra da segunda palavra (w)