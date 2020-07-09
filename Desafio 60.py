print('====== DESAFIO 60 ======')
num = 1
valor = int(input('Digite um número: '))
fatorial = valor
while valor >= 1:
    num = num * valor
    valor += -1
    print(f'{valor+1} x ',end='')
print(f'O fatorial de {fatorial} é: {num}')