print('========================')
print('        BANCO CEV       ')
print('========================')
while True:
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    valor = int(input('Digite o valor a ser sacado: '))
    print('')
    while valor < 1000:
        print('ERRO! Valor permitido a ser sacado a partir de R$1000 ')
        valor = int(input('Digite o valor a ser sacado: '))
        print('')
    while valor > 9999:
        print('ERRO! Valor a ser sacado é alto demais. Tente um valor menor')
        valor = int(input('Digite o valor a ser sacado: '))
        print('')
    milhar = ((valor // 1000) % 10) * 1000
    centena = ((valor // 100) % 10) * 100
    dezena = ((valor // 10) % 10) * 10
    unidade = ((valor // 1) % 10) * 1
    
    for c in range(1, milhar+1, 50):
        cont += 1
    print(f'TOTAL DE: {cont} cédulas de R$50,00')

    for c in range(1, centena+1, 20):
        cont1 += 1
    print(f'TOTAL DE: {cont1} cédulas de R$20,00')

    for c in range(1, dezena+1, 10):
        cont2 += 1
    print(f'TOTAL DE: {cont2} cédulas de R$10,00')

    for c in range(1, unidade+1, 1):
        cont3 += 1
    print(f'TOTAL DE: {cont3} cédulas de R$1,00')
    print('')
    parada = str(input('Deseja sacar outro valor? [S/N] ')).upper()
    print('')
    while parada != 'S' and parada != 'N':
        print('ERRO! Valor digitado não reconhecido. Tente Novamente')
        parada = str(input('Deseja sacar outro valor? [S/N] ')).upper()
        print('')
    if parada == 'N':
        print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
        break
