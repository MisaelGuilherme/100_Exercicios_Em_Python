print('====== DESAFIO 29 ======')
speed = int(input('Digite a velocidade do veículo: '))
if speed > 80:
    print('Multado por excesso de velocidade!')
    calc = speed - 80
    print('Sua multa é de: R${}'.format(calc))
else: 
    print('Limite de velocidade ok.')    