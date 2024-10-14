#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo',
         'Cruzeiro', 'Fortaleza', 'Athletico-PR', 'Red Bull Bragantino',
         'Atlético-MG', 'Vasco', 'Internacional', 'Juventude', 'Criciúma',
         'Vitória', 'Cuiabá', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')
print('-=-'*30)
print(f'Os 20 primeiros times do brasileirão são: {times}')
print('-=-'*30)
print(f'Os 5 primeiros times são: {times[:5]}')
print('-=-'*30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=-'*30)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('-=-'*30)
if 'Chapecoense' in times:
    print(f'O time de Chapecoense está na {times.index('Chapecoense')}° posição')
else:
    print('O time de Chapecoense não está entre os 20 primeiros colocados')
