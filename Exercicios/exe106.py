# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
from time import sleep

cores = (
    '\033[0m',      # 0 > texto cor padrão
    '\033[93m',     # 1 > texto cor amarelo
    '\033[94m',     # 2 > texto cor azul
    '\033[91m',     # 3 > texto cor vermelha
    '\033[30;47m'   # 4 > texto preto com fundo branco
)
def titulo(texto, cor = 0):
    tam = len(texto) + 4
    print(cores[cor] + '-' * tam)
    print(f'  {texto}')
    print('-' * tam + cores[0])
    sleep(1)

def getInputUser():
    opcao = input('Função ou Bliblioteca > ').strip().lower()
    return opcao

def helpPython():
    titulo('Sistema de Ajuda PyHelp', 1)
    while True:
        opcao = getInputUser()
        if opcao == 'fim':
            titulo('Até Logo!', 3)
            return
        titulo(f'Acessando o manual do comando \'{opcao}\'', 2)
        print(cores[4], end='')
        print(help(opcao))
        print(cores[0], end='')
        sleep(2)


# Principal
helpPython()
