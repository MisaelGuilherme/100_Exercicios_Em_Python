print('====== DESAFIO 78 ======')
lista = list()
cont = 0
for c in range(1,3):
    lista.append(int(input('Digite um número: ')))
print(f'O maior número digitado foi: {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor número digitado foi: {min(lista)} na posição {lista.index(min(lista))}')