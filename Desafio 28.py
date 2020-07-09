from random import randint
print('====== DESAFIO 28 ======')
attempt = int(input('Digite um número de 0 a 5: '))
aleatory = randint(0,5)
if attempt == aleatory:
    print('Parabéns você acertou!!! :)')
    print('O número era: {}'.format(aleatory))
else:
    print('Você não acertou. :( ')
    print('O número era: {}'.format(aleatory))