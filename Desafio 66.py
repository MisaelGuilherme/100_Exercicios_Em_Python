print('====== DESAFIO 66 ======')
cont = 0
soma = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'A quantidade de números digitados foi: {cont}')
print(f'A soma de todos os valores é: {soma}')