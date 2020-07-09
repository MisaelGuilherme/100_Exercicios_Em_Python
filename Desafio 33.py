print('====== DESAFIO 33 ======')
scanner = int(input('Digite o primeiro valor: '))
scanner2 = int(input('Digite o segundo valor: '))
scanner3 = int(input('Digite o terceiro valor: '))
if scanner > scanner2 and scanner > scanner3:
    print('{} é o numéro maior'.format(scanner))
elif scanner2 > scanner and scanner2 > scanner3:    
    print('{} é o numéro maior'.format(scanner2))
elif scanner3 > scanner and scanner3 > scanner2:
    print('{} é o numéro maior'.format(scanner3))
else: 
    print('Não existe número maior')
#----------------------------------------------    
if scanner < scanner2 and scanner < scanner3:
    print('{} é o numéro menor'.format(scanner))
elif scanner2 < scanner and scanner2 < scanner3:    
    print('{} é o numéro menor'.format(scanner2))
elif scanner3 < scanner and scanner3 < scanner2:
    print('{} é o numéro menor'.format(scanner3))    
else:
    print('Não existe número menor')     