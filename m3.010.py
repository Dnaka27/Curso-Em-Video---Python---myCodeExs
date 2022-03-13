print("Situação escolar")
print("-" * 30)
aluno = {}
aluno["Nome"] = str(input("Digite o nome do aluno: "))
aluno["Nota"] = float(input("Digite a nota do aluno: "))
if aluno["Nota"] >= 7:
    aluno["Nituação"] = "Aprovado"
elif aluno["Nota"] < 7 and aluno["Nota"] >= 5:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"
print("-" * 30)
for k, v in aluno.items():
    print(f"\t - {k}: {v}")