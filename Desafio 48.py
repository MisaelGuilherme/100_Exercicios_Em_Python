print('====== DESAFIO 48 ======')
s = 0
for c in range(1, 501):
    value = c*3
    if value % 2 == 0:
        print(c,'x 3 % 2 = PAR')
    else:
        print(c,'x 3 % 2 = IMPAR')