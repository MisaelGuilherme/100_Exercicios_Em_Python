print('====== DESAFIO 64 ======')
value = 0
num = 0
soma = 0
while value != 999:
    value = int(input('Digite um valor: '))
    if value == 999:
        break
    num += 1
    soma += value
print('O valor 999 foi digitado!')
print(f'A quantidade números digitados foi: {num}')
print(f'A soma de todos os números digitados foram: {soma}')