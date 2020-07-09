print('====== DESAFIO 58 ======')
from random import randint
aleatory = randint(1,10)
palpite = 0
print('-----TENTE ACERTAR-----')
acert = int(input('Digite Um Número Entre.. 1 a 10: '))
while acert != aleatory:
    print('Você Não Venceu a Máquina.. :(')
    acert = int(input('Tente novamente: '))
    palpite += 1
if acert == aleatory:
    print('Parabéns Você Venceu a Máquina! :D')
    print(f'Palpites: {palpite}')