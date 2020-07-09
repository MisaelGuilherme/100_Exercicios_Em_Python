print('====== DESAFIO 65 ======')
s = 1
cont = 0
soma = 0
maiorValor = 0
menorValor = 0
while s == 1:
    valor = int(input('Digite um número: '))
    if maiorValor == 0 and menorValor == 0:
        maiorValor = valor
        menorValor = valor
    if valor > maiorValor:
        maiorValor = valor
    if valor < menorValor:
        menorValor = valor
    cont += 1
    soma += valor
    s = int(input('Deseja continuar [s] = 1 , [n] = 0: ' ))
media = soma/cont
print(f'O valor total de número digitados foi: {cont}')
print(f'A média é: {media}')
print(f'O maior valor é: {maiorValor}')
print(f'O menor valor é: {menorValor}')