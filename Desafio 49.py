print('====== DESAFIO 49 ======')
print('[1] = SOMA')
print('[2] = SUBTRAÇÃO')
print('[3] = MULTIPLICAÇÃO')
print('[4] = SUBTRAÇÃO')
print('')
number = int(input('DIGITE A OPERAÇÃO: '))
if number == 1:
    value = int(input('Digite um número: '))
    for c in range (1, value+1):
        s = value + c
        print(value,'+',c,'=',s)
if number == 2:
    value = int(input('Digite um número: '))
    for c in range (1, value+1):
        s = value - c
        print(value,'-',c,'=',s)
if number == 3:
    value = int(input('Digite um número: '))
    for c in range (1, value+1):
        s = value * c
        print(value,'*',c,'=',s)
if number == 4:
    value = int(input('Digite um número: '))
    for c in range (1, value+1):
        s = value / c
        print(value,'/',c,'=',s)