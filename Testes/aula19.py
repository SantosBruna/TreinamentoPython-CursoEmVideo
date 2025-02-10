pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22} #tupla=(), lista=[]

print(f'O{pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
print(pessoas.items())
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
####################################
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estados = dict()
brasil = list()
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estados.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print((f'O campo {k} tem o valor {v}'))
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
