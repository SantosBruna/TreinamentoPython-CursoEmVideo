def aumentar(num=0, taxa=10, formata=False):
    '''
    Função para somar uma taxa (%) a um valor
    :param num: Valor a ser somado a uma taxa
    :param taxa: Taxa que será aumentada
    :param formata: Se precisa ou não retornar o valor já formatado. Por padrão é False
    :return: retorna o número mais a taxa
    '''
    valor_final = ((num * taxa)/100) + num
    if formata == True:
        return moeda(valor_final)
    else:
        return valor_final

def diminuir(num=0, taxa=10, formata=False):
    '''
    Função para diminuir uma taxa (%) de um valor
    :param num: O valor que será diminuido
    :param taxa: taxa que será usada para diminuir o valor
    :param formata: Se precisa ou não retornar o valor já formatado. Por padrão é False
    :return: retorna o número menos a taxa
    '''
    valor_final = num - ((num * taxa)/100)
    if formata == True:
        return moeda(valor_final)
    else:
        return valor_final

def dobro(num=0, formata=False):
    '''
    Função para retornar o dobro de um número
    :param num: Um número que será usado para retorno do dobro
    :param formata: Se precisa ou não retornar o valor já formatado. Por padrão é False
    :return: Retorna o dobro de um número
    '''
    num *= 2
    if formata == True:
        return moeda(num)
    else:
        return num


def metade(num=0, formata=False):
    '''
    Função que retorna a metade de um número
    :param num: O número que será divido
    :param formata: Se precisa ou não retornar o valor já formatado. Por padrão é False
    :return: Retorna a metade de um número
    '''
    num /= 2
    if formata == True:
        return moeda(num)
    else:
        return num

def moeda(num=0, moeda='R$'):
    '''
    Função que retorna um número formatado ao estilo moeda
    :param num: Número que será formatado
    :param moeda: String com o estilo da moeda. Por padrão é 'R$'
    :return: retorna uma string com o estilo da moeda na frente e o número com duas casas decimais e vírgula ao invés de ponto. Retorna uma string
    '''
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=0, aumento=10, reducao=5):
    dobro_num = dobro(num, True)
    metade_num = metade(num, True)
    num_aumento = aumentar(num, aumento, True)
    num_diminui = diminuir(num, reducao, True)
    print('=' * 40)
    print('Resumo do Valor'.center(30))
    print('=' * 40)
    print(f'Preço Analisado:\t{moeda(num)}')
    print(f'Dobro do preço:\t\t{dobro_num}')
    print(f'Metade do preço:\t{metade_num}')
    print(f'{aumento:.0f}% de Aumento:\t\t{num_aumento}')
    print(f'{reducao:.0f}% de redução:\t\t{num_diminui}')
    print('=' * 40)
