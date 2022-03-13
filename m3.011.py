from random import randint
from time import sleep
from operator import itemgetter

print("Jogo de dados")
print("-" * 30)
jogo = {"jogador 1": randint(1,6),
        "jogador 2": randint(1,6),
        "jogador 3": randint(1,6),
        "jogador 4": randint(1,6)}
ranking = []
print("Valore sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print(ranking)
print("-" * 30)
print("\t RANKING")
for p, v in enumerate(ranking):
    print(f"{p+1}° lugar: {v[0]} tirou {v[1]} no dado")
    sleep(1)