print('====== DESAFIO 67 ======')
digt = 0
while True:
    valor = int(input('Deseja saber a tabuada de qual número? '))
    if valor < 0:
        break
    for c in range(1, 11):
        mult = c*valor
        print(f'{valor} X {c} = {mult}')
print('Obrigado por usar a nossa Calculadora!')