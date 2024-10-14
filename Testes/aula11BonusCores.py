'''Códigos de style:
0 => nenhum
1 => Bold(negrito)
4 => underline(sublinhado)
7 => negative(inverte o que vc colocou
para letra vai pra fundo e o que vc colocou para fundo vai para letra)

Text:
30 => branco
31 => vermelho
32 => verde
33 => amarelo
34 => azul
35 => lilas
36 => ciano
37 => cinza

Background:
40 => branco
41 => vermelho
42 => verde
43 => amarelo
44 => azul
45 => lilas
46 => ciano
47 => cinza
*** preto é a cor padrão no fundo

\033[7;30m => esse código gera um fundo branco com letra preta.
Como o código 30 é letra branca, o 7 que é o inversor inverte a cor e ela fica preta.'''

print('\033[4;30;45mOlá mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32{} e \033[31{}\033[m!!!'.format(a, b))

nome = 'Bruna'
cores = {'limpa':   '\033[m',
         'azul':    '\033[34m',
         'amarelo': '\033[33m',
         'preto':   '\033[0;30m' }
#print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['preto'], nome, cores['limpa']))



