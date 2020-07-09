print('====== DESAFIO 57 ======')
sexo = str(input('Digite seu sexo - [F][M] :')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo não reconhecido!')
    sexo = str(input('Digite seu sexo: ')).upper()
print(f'Seu sexo é: {sexo}')