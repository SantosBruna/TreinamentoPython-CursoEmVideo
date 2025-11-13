# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
import math


def fatorial(numero, show=False):
    """
        → Calcula o fatorial de um número.
        :param numero: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
        :return: Sem retorno
    """
    resultado = 0
    if show == True:
        for i in range(numero, 0, -1):
            if i == numero:
                resultado = numero
                print(f'{numero}! = {numero}', end=' ')
            else:
                resultado *= i
                print(f'x {i}', end=' ')
        print(f' = ', end=' ')
        return resultado
    else:
        resultado = math.factorial(numero)
        return resultado

#princiapal
help(fatorial)
num = int(input('Informe um número: '))
print(fatorial(num, show=True))
