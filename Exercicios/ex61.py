#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
c = 0
pa = termo

while c < 10:
    print('{}'.format(pa), end='-> ')
    pa = pa + razao
    c += 1
print('FIM', end='')
