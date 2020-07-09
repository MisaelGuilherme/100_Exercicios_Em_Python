print('====== DESAFIO 68 ======')
print('=-=-=-=-=-=- VAMOS JOGAR PAR OU ÍMPAR =-=-=-=-=-=-=')
from random import randint
vitorias = 0
while True:
    jog = int(input('DIGITE UM VALOR: '))
    escolhe = int(input('DESEJA SER: PAR[1] OU IMPAR[2]: '))
    pc = randint(0, 10)
    contagem = (jog + pc) % 2
    soma = pc + jog
    if contagem == 0:
        resultado = 'PAR'
        n = 1
    else:
        resultado = 'ÍMPAR'
        n = 2
    print('')
    print(f'JOGADOR LANÇOU: {jog}')
    print(f'MÁQUINA LANÇOU: {pc}')
    print(f'RESULTADO: {soma} = {resultado}')
    if n == escolhe:
        print('JOGADOR VENCEU MÁQUINA!')
        vitorias += 1
        print(f'VITÓRIAS: {vitorias}')
    else:
        print('MÁQUINA VENCEU JOGADOR!')
        print(f'VITÓRIAS: {vitorias}')
        break
    print('')