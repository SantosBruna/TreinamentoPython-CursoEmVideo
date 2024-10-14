#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Um ano é bissexto se for divisível por 4.
#No entanto, se o ano for divisível por 100, ele não é bissexto, a menos que:
#O ano seja também divisível por 400. Nesse caso, ele é bissexto.

from datetime import date
ano = int(input('Informe o ano que deseja analisar ou digite 0 para verificar o ano atual: '))

if ano == 0:
    data = date.today()
    ano = data.year
print('O ano informado é {}'.format(ano))
# if(ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0)
if( ano % 4 == 0):
    if (ano % 100 == 0):
        if(ano % 400 == 0):
            print('O ano {} é bissexto!'.format(ano))
        else:
            print('O ano {} não é bissexto!'.format(ano))
    else:
        print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
