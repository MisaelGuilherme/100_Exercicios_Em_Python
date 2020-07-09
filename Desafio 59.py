print('====== DESAFIO 59 ======')
escolha = 2
opcao =  0
while escolha == 2:
    valor = int(input('Digite 1º valor: '))
    valor2 = int(input('Digite o 2º valor: '))
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Reiniciar')
    print('[6] Sair')
    opcao = int(input('Qual Operação Deseja Realizar: '))
    if opcao == 1:
        result = valor + valor2
        print(f'O resultado de {valor} + {valor2} é igual: {result}')
    elif opcao == 2:
        result = valor - valor2
        print(f'O resultado de {valor} - {valor2} é igual: {result}')
    elif opcao == 3:
        result = valor * valor2
        print(f'O resultado de {valor} * {valor2} é igual: {result}')
    elif opcao == 4:
        result = valor / valor2
        print(f'O resultado de {valor} / {valor2} é igual: {result}')
    elif opcao == 5:
        print('Reinciando...')
        if escolha == 5:
            escolha = 5
    elif opcao == 6:
        print('[x]Programa Encerrado!')
        break
    