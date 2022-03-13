import Functions014a as f014
from time import sleep

print("Criando menu")
print("-" * 30)

while True:
    resposta = f014.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        print("Opção 1")
    elif resposta == 2:
        print("Opção 2")
    elif resposta == 3:
        print("Saindo do sistema... Até logo")
        break
    else:
        print("\033[31mERRO: Digite uma opção válida\033[m")
    sleep(1.5)