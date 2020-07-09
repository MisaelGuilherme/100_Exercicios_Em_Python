print('====== DESAFIO 34 ======')
salary = float(input('Digite o seu salário atual: '))
if salary > 1250:
    calc = (salary * 10)/100
    result = salary + calc
    print('O seu novo salário é: {}'.format(result))
else:
    calc = (salary * 15)/100
    result =(salary + calc)
    print('O seu novo salário é: {}'.format(result))