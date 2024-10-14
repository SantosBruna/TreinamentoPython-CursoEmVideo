#tuplas são imutáveis no python, pode ser sem parenteses que o python entende que é uma tupla
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(sorted(lanche))#Vai ordernar a tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)#vai unir as tuplas, tupla a vem depois da b
print(c.count(5))#quantas vezes o número 5 aparece dentro de c
print(c.index(8))#em que posição está o número 8 na tupla?ele pega a primeira ocorrencia
print(c.index(5, 1))#ele procura a posição a partir do termo que está na posição 1
pessoa = ('Bruna', 36, 'F', 74)
del(pessoa)#ele apaga a tupla chamada pessoa
