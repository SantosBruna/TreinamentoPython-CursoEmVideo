n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma é {}'.format(s))
print(f'A soma vale {s}')
nome = 'Jose'
idade = 33
salario = 987.3
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')