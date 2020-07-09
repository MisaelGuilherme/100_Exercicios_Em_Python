print('====== DESAFIO 55 ======')
maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi: {maior} kg')
print(f'O menor peso foi: {menor} kg')