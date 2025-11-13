#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(texto):
    ok = False
    while ok is False:
        num = str(input(texto))
        if num.isnumeric():
            ok = True
        else:
            print('\033[91mERRO! Digite um número inteiro válido\033[0m')
    return num





# Programa principal
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')
