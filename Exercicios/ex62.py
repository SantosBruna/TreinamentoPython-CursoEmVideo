#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
c = 1
pa = termo
cont = 10
limit = 10
while c <= limit and c != 0:
    print('{}'.format(pa), end='-> ')
    pa = pa + razao
    c += 1
    if c > limit:
        print('PAUSA', end='')
        limit = int(input("\nQuantos mais termos desta progressão deseja ver? "))
        c = 1
        cont += limit
print("A progressão foi finalizada com {} termos mostrados.".format(cont))
