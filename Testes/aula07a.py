#Ordem de precedência
#1 ()
#2 **
#3 *  /  //  %
#4 + -

#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é:  {} ' .format(s))
print('A multiplicação é: {}' .format(m))
print('A divisão inteira é: {}' .format(di))
print('A exponenciação é: {}' .format(e))

