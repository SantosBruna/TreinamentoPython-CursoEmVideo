#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: '))

a = str.count(expressao, "(")
b = str.count(expressao, ")")

if expressao.index(')') > expressao.index('('):
    if a == b:
        print("a expressão está correta!")
    else:
        print("A expressão está incorreta!")
else:
    print("A expressão está incorreta!")

