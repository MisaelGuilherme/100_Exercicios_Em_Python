print('====== DESAFIO 80 ======')
lista = list()
var = 0
vari = 0
for cont in range(1,4):
    value = int(input('Digite um valor: '))
    var = value
    if value < var:
        var = value
    if value > var:
        vari = value
print('MAIOR =',var)
print('MENOR =',vari)