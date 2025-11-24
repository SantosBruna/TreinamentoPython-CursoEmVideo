#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*nota, sit=False):
    """
     → Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais nota dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    media_notas = sum(nota)/len(nota)
    dic_notas = {
        'total': len(nota),
        'maior': max(nota),
        'menor': min(nota),
        'media': media_notas,
    }

    if sit == True:
        if media_notas < 6:
            dic_notas['situação'] = 'RUIM'
        elif media_notas > 7:
            dic_notas['situação'] = 'BOA'
        elif 7 > media_notas >= 6:
            dic_notas['situação'] = 'RAZOAVEL'
    return dic_notas





### Principal
print(notas(5.5, 9.5, 10, 6.6, sit=True))
help(notas)

