# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: '))
           )

print(f'Os valores digitados foram {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 apareceu na posição {numeros.index(3) + 1}°')
else:
    print('O número 3 não esta na tupla')
print('Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
