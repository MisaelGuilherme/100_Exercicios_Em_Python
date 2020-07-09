print('====== DESAFIO 31 ======')
trip = float(input('Informe em KM a distância da viagem:  '))
if trip <=200:
    passagem = 0.50*trip
    print('O valor da passagem custará: {}'.format(passagem))
else:
    passagem = 0.45*trip
    print('O valor da passagem custará: {}'.format(passagem))