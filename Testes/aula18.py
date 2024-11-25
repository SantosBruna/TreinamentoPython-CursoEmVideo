teste = list()
teste.append('Bruna')
teste.append(36)
galera = list()
galera.append(teste[:])
#galera.append(teste)#aqui é criado uma ligação entre as listas, de forma que se a primeira for alterada a segunda também será modificada
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #desta forma os dados são copiados para a segunda lista mas se alterarmos a primeira lista a segunda não será alterada.
print(galera)

#outra forma de criar listas dentro de listas:

grupo = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in grupo:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera2 = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)

for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')




