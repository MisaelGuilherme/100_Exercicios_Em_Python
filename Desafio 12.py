print('====== DESAFIO 12 ======')
preco = int(input('Informe o preço do produto: '))
calc = (5*preco)/100
valor_atual = preco - calc
print('Com Desconto de 5% ....')
print('O valor passará a ser {}:'.format(valor_atual))
