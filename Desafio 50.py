print('====== DESAFIO 50 ======')
s = 0
for c in range(1,6):
    receive = int(input('Digite um valor: '))
    if receive % 2 == 0:
        s += receive
    else:
        s += 0        
print(s)