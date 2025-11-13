# Interactive Help
# docstrings
# argumentos opcionais
# escopo de variáveis
# retorno de resultados

##Interactive Help

help(input)
print(input.__doc__)


##Docstring = string de documentação

def contador(i, f, p):
    """
        → Faz uma contagem e mostra na tela.
        :param i: Inicio da contagem
        :param f: Fim da contagem
        :param p: Passo da contagem
        :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='..')
        c += p
    print('FIM')


#contador(2, 10, 2)
help(contador)

##Parametros opcionais

def soma(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma é {soma}')


soma(3, 2, 5)
soma(8, 4)
soma()
soma(b=4, c=2)
soma(c=3, a=2)
print()

##Escopo de variáveis = toda variavel criada no programa principal será reconhecida por qualquer função
## mas as variáveis criadas dentro da função não são reconhecidas no programa princpal,
## elas vão existir somente dentro da função a qual foi criada. Neste caso podemos dizer que a variavel do programa principal possui escopo global,
## ja a variável criado dentro da função dizemos que possui um escopo local
def test():
    global a
    a = 7 #-> como foi declarado 'global a' na linha de cima, aqui não será criado uma outra variável chamada a,
            # será usada a mesma variável que foi criada no programa principal.
    n = 8 #-> variável local com o nome de n valendo 8. Neste caso se dermos um print a variável n exibida será a do escopo local, com valor 8.
    c = 5 #-> variável local com o nome de c valendo 5
    print(f'Na função teste, n vale {n}')

#Programa Principal
n = 2 #->variável global com o nome n valendo 2
a = 5 #->variável global com o nome a valendo 5
print(f'No programa principal, n vale {n}')
test()
print()

##Retorno de Valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2,5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram: {r1}, {r2} e {r3}.')
print()


###EXERCÍCIOS
print("------EXERCICIOS DE FIXAÇÃO------")
print()
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}.')
print()
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')


