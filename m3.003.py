print("Contando vogais")
palavras = ("Aprender", "crescer", "evoluir")
for i in palavras:
    print(f"\nNa palavra {i} temos, como vogais: ", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
            