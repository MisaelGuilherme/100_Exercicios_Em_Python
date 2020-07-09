print('====== DESAFIO 35 ======')
value1 = float(input('1ª reta do triângulo:[lado A] : '))
value2 = float(input('1ª reta do triângulo:[lado B] : '))
value3 = float(input('3ª reta do triângulo:[lado c] : '))
if value1 + value2 > value3:
    print('{} + {} > {} É possível formar um triângulo.'.format(value1, value2, value3))
else:
    print('{} + {} < {} NÃO possível formar um triângulo.'.format(value1, value2, value3))