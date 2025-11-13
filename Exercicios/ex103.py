# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def string_to_int(valor):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return 0
def ficha(nome='<desconhecido>', gols=0):
    gols = string_to_int(gols)
    if nome == '':
        nome = '<desconhecido>'
    elif gols == '':
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'



# Principal
jogador = str(input('Informe o nome do jogador: ')).capitalize()
qtd_gols = input('Informe o n° de gols: ')
print('-=-' * 20)
print(ficha(jogador, qtd_gols))
