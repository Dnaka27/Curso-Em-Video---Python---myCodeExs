from math import radians, sin, cos, tan
an = float(input("Digite o angulo desejado: "))
print("================================")
seno = sin(radians(an))
print("O angulo de {}° tem o seno de {:.2f}" .format(an, seno))
print("================================")
cosseno = cos(radians(an))
print("O angulo de {}° tem o cosseno de {:.2f}" .format(an, cosseno))
print("================================")
tangente = tan(radians(an))
print("O angulo de {}° tem tangente de {:.2f}" .format(an, tangente))
print("================================")
