# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# Voto proibido (negado): Menores de 16 anos não podem votar
# Voto facultativo (opcional): 16 e 17 anos (menores de idade)
# Voto obrigatório: Entre 18 e 70 anos (incompletos)

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - int(ano)

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade <= 17:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

# principal:


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
