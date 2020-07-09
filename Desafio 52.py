print('====== DESAFIO 51 ======')
receive = int(input('Digite um número: '))
tot = 0
for c in range(1, receive+1):
    s = receive % c
    if s == 0:
        tot += 1
if tot > 2:
    print(receive,'Não é primo')
else: 
    print(receive,'É primo')    