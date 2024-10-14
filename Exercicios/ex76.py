#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos =('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Régua', 10, 'Compasso', 9.99, 'Mochila', 150, 'Canetas', 10, 'Livro', 50)

print('='*40)
print(f'{"Listagem de preços":^40}')
print('='*40)
for pos in range(0, len(produtos), 2):
    print(f'{produtos[pos]:-<30}', end='')
    print(f' R${produtos[pos + 1]:>7.2f}')
