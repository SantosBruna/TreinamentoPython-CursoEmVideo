#Faça um programa que leia algo pelo
# teclado e mostre na tela o seu tipo primitivo e
#todas as informações possíveis sobre ele

x = input('Digite algo: ')
print('O tipo deste valor é: ', type(x))
print('Ele é um número? ', x.isnumeric())
print('Ele é um valor alfabético? ', x.isalpha())
print('Ele é um valor alfa numérico? ', x.isalnum())
print('Ele pode ser impresso? ', x.isprintable())
print('Ele só tem espaço? ', x.isspace())
print('Ele está em maiúsculo? ', x.isupper())
print('Ele está em minúsculo? ', x.islower())
print('Ele está capitalizado? ', x.istitle()) #quando uma letra é maiúscula e as outras são minúsculas

