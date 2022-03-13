from Functions014a import *
from Functions014b import *
from time import sleep


print("Criando menu")
print("-" * 30)

arq = "CursoEmVideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo")
        break
    else:
        print("\033[31mERRO: Digite uma opção válida\033[m")
    sleep(1.5)