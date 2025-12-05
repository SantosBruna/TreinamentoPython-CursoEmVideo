def leiaDinheiro():
    while True:
        preco = input('Digite o preço: R$').strip()
        if ',' in preco:
            preco = float(preco.replace(',', '.'))
            return preco
        if '.' in preco:
            return float(preco)
        elif preco.isnumeric():
            return float(preco)
        else:
            print(f'\033[91mErro! "{preco}" é um preço inválido!\033[0m ')
