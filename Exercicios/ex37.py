#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
print('-=-' * 20)
print('Conversão de número inteiro!')
print('*' * 30)
print('Bases para a conversão: \n[1] para binário\n[2] para octal\n[3] para hexadecimal')
print('-=-' * 20)
numero = int(input('Informe um número inteiro: '))
base = int(input('Qual será a base de conversão? '))

if base == 1:
    conversao = bin(numero)
    print('O número informado foi {}, convertido para a base 2 temos {}'.format(numero, conversao[2:]))
elif base == 2:
    conversao = oct(numero)
    print('O número informado foi {}, convertido para a base 8 temos {}'.format(numero, conversao[2:]))
elif base > 3:
    print('Número da base informado errado! Escolha uma dentre as opções!')
else:
    conversao = hex(numero)
    print('O número informado foi {}, convertido para a base 16 temos {}'.format(numero, conversao[2:]))
