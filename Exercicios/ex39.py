#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano = int(input('Ano de nascimento: '))
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
idade = ano_atual - ano

print('A idade informada é {} anos em {}'.format(idade, ano_atual))
if idade < 18:
    x = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(x))
    print('Seu alistamento será em {}'.format(ano_atual + x))
elif idade == 18:
    print('Você deve se alistar ao serviço militar IMEDIATAMENTE')
else:
    x = idade -18
    print('Você já deveria ter se alistado há {} anos'.format(x))
    print('Seu alistamento foi em {}'.format(ano_atual - x))
