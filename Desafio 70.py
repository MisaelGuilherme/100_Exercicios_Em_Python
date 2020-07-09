print('====== DESAFIO 70 ======')
total = 0
produtoMaior = 0
produtoBarato = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    if produtoBarato == 0:
        produtoBarato = preco
        nomeProduto = nome
    if preco < produtoBarato:
        produtoBarato = preco
        nomeProduto = nome
    total += preco
    if preco > 1000:
        produtoMaior += 1
    parada = str(input('Deseja continuar [S/N]: ')).upper()
    while parada != 'S' and parada != 'N':
        parada = str(input('Deseja continuar [S/N]: '))
    if parada == 'N':
        break
print('')
print(f'O valor total foi: {total}')
print(f'Produtos maiores de R$1000: {produtoMaior}')
print(f'O produto mais barato foi: {nomeProduto} por R${produtoBarato}')