# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dessezeis', 'dessesete', 'dezoito',
           'dezenove', 'vinte')

while True:
    num = ' '
    while num not in range(0, 21):
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o numero {numeros[num]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N}')).strip().upper()[0]
    if resp == 'N':
        break
print('Programa encerrado, volte sempre!')


