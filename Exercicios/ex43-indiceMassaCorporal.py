# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida
from time import sleep

print('-=-'*20)
print('ÍNDICE DE MASSA CORPORAL')
print('-=-'*20)
peso = float(input('Informe o seu peso: (kg) '))
altura = float(input('Informe a sua altura: (m) '))
print('Calculando...')
sleep(1)
imc = peso / altura**2
print('O resultado do Índice de massa corporal é {:.1f}'.format(imc))

if imc < 18.5:
    print('O resultado do seu IMC é: Abaixo do peso')
elif imc < 25:
    print('O resultado do seu IMC é: Peso Normal')
elif imc < 30:
    print('O resultado do seu IMC é: Sobrepeso')
elif imc < 40:
    print('O resultado do seu IMC é: Obsesidade')
else:
    print('O resultado do seu IMC é: Obesidade mórbida')

