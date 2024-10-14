# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('caderno', 'abacate', 'metal', 'aprender', 'programar', 'linguagem', 'python', 'estudar', 'gratis', 'trabalhar')

for item in lista:
    print(f'\n{item:-<20}Vogais: ', end='')
    for letra in item:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=', ')
