#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


maior = homens = mulheres = 0
while True:
    print('-' * 20)
    idade = int(input('Informe a idade da pessoa: '))
    sexo = resp = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o gênero dela? [F/M] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1

    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{maior} pessoas tem mais de 18 anos, sendo {homens} homens.')
print(f'{mulheres} mulheres possuem menos de 20 anos')
