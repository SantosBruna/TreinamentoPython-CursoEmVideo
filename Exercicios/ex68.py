#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-=-'*20)
print('VAMOR JOGAR PAR OU ÍMPAR!')
print('-=-'*20)

v = 0
while True:
    num_jogador = int(input('Qual o seu número? '))
    computador = randint(1, 10)
    total = num_jogador + computador
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*20)
    print(f'Você jogou {num_jogador} e o computador jogou {computador} o total foi {total}')
    print('-' * 20)
    if total % 2 == 0 and jogador == 'P':
        print('Deu PAR! Você venceu!')
        v += 1
    elif total % 2 != 0 and jogador == 'I':
        print('Deu ÍMPAR! Você venceu!')
        v += 1
    elif total % 2 == 0 and jogador == 'I':
        print('Você Perdeu! Deu PAR')
        break
    elif total % 2 != 0 and jogador == 'P':
        print('Você Perdeu! Deu íMPAR')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')