print('====== DESAFIO 79 ======')
lista = list()
user = 's'
while user == 's':
    n = int(input('Digite um valor: '))
    value = lista.count(n)
    if value < 1*1:
        lista.append(n)
        print('Valor adicionando com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    user = str(input('Deseja continuar? [S/N]')).lower()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Você digitou os valores:',lista)