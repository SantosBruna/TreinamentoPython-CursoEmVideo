#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#formula (0 °C × 9/5) + 32 = 32 °F

celsius = int(input('Informe a temperatura em graus Celsius: '))

far = celsius * 9 / 5 + 32

print('A temperatura {}°C em Celsius convertida é {}°F'.format(celsius, far))
