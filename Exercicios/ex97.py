# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(txt):
    espaco = len(txt) + 4
    print('~' * espaco)
    print(f'{txt:^{espaco}}')
    print('~' * espaco)


#programa principal

escreva('Gustavo Guanabara')
escreva('Curso de Python no YoutTube')
escreva('CeV')
