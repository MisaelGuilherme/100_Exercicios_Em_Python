print('====== DESAFIO 61 ======')
num = 1
sim = 1
while sim == 1:
    receive = int(input('Digite o número da contagem: '))
    receive2 = int(input('Digite o numero de intervalo: '))
    while num < receive:
        print(num)
        num += receive2
    print('')
    sim = int(input('[1] Mostrar Mais um Termo - [0] Mostrar 0 Termo: '))
    if sim == 0:
        print('[x] Programa Finalizado!')