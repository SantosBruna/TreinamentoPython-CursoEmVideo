#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa


x = float(input('Digite um número: '))
y = float(input('Digite outro número: '))
print((' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos Números\n [5] Sair do programa'))

menu = int(input('Informe a opção desejada: '))
while menu != 5:
    if menu == 0 or menu > 5:
        print('Opção errada')
    elif menu == 1:
        print('{:.0f} + {:.0f} = {:.0f} '.format(x, y, x + y))
        print('-=-'*20)
    elif menu == 2:
        print('{:.0f} X {:.0f} = {:.0f}'.format(x, y, x * y))
        print('-=-' * 20)
    elif menu == 3:
        if x > y:
            print('{:.0f} > {:.0f}'.format(x, y))
        elif x < y:
            print('{:.0f} > {:.0f}'.format(y, x))
        else:
            print('{:.0f} = {:.0f}'.format(y, x))
        print('-=-' * 20)
    elif menu == 4:
        x = float(input('Digite um novo número: '))
        y = float(input('Digite outro número novo: '))
        print('-=-' * 20)
    menu = int(input('Informe a opção desejada: '))
