#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('De qual número deseja ver a tabuada? '))
    if n < 0:
        break
    c = 1
    print(f'-' * 20)
    while c <= 10:
        print(f'{n} X {c} = {n * c}')
        c += 1
    print(f'-' * 20)
print('Programa de tabuada encerrado, volte sempre!')