num = [2, 5, 9, 1]
num.append(7)#coloca o 7 dentro da lista
num.sort()#coloca na ordem crescente
num.sort(reverse=True)#coloca na ordem decrescente
num.insert(2, 0)#coloca o número 0 na posição 2
num.pop(2)#remove o elemento com o indice 2, sem colocar o numero remove o último elemento
num.insert(2, 2)
num.remove(2) #remove o primeiro número 2 que achar na lista
valores=list(range(4, 11))

if 3 in num:
    num.remove(3)#com o if agente consegue verificar se o elemento existe na lista antes de tentar remover ele.
else:
    print('Não achei o número 3')
    
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#as duas listas terão os valores da posição 2 alterados, pois foi declarado que elas são iguais
c = a[:] #desta forma ele só copia os dados, não faz a ligação que foi feito na lista b
