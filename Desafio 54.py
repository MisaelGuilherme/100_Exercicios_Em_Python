print('====== DESAFIO 54 ======')
biggerAge = 0
smallerAge = 0
for yearBirth in range(0, 7):
    age = int(input('Digite a sua idade: '))
    if age >= 21:
        biggerAge += 1
    else:
        smallerAge += 1
print(f'{smallerAge} Pessoas ainda não atingiram a maior idade')
print(f'{biggerAge} Pessoas já atingiram a maior idade')