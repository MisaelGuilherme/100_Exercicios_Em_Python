'''print('====== DESAFIO 23 ======')
cont = str(input('Digite o valor: '))
ler = len(cont)
while ler < 4:
    cont = str(input('Digite um valor: '))
    fonte = len(cont)
    if fonte == 4:
        print('Milhar: {}'.format(cont[0]))
        print('Centena: {}'.format(cont[1]))
        print('Dezena: {}'.format(cont[2]))
        print('Unidade: {}'.format(cont[3]))
print('Milhar: {}'.format(cont[0]))
print('Centena: {}'.format(cont[1]))
print('Dezena: {}'.format(cont[2]))
print('Unidade: {}'.format(cont[3]))'''

num = int(input('Digite um valor: '))
calc = num // 1000 % 10
calc1 = num // 100 % 10
calc2 = num // 10 % 10
calc3 = num // 1 % 10
print('Milhar: {}'.format(calc))
print('Centena: {}'.format(calc1))
print('Dezena: {}'.format(calc2))
print('Unidade: {}'.format(calc3))