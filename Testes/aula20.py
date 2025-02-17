def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(*num): #cria uma tupla com os valores recebidos
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def somando(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

# Programa Principal
titulo(' CURSO EM VÍDEO')
titulo(' FUNÇÕES')
titulo(' BRUNA SR SANTOS')

soma(4, 5)
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
somando(5, 2)
somando(2, 9, 4)

