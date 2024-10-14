#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Informe o nome da cidade em que nasceu')).strip()

lista = cidade.upper().split()
result = 'SANTO' in lista[0]
print(result)

