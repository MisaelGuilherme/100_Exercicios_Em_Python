print('====== DESAFIO 27 ======')
name = (input('Digite seu Nome e Sobrenome: ')).capitalize()
receive1 = name.split()
print('Seu Primeiro Nome é: {}'.format(receive1[0]))
receive2 = name.split()
learning = len(receive2)
print('Seu Último Nome é: {}'.format(receive2[learning-1]))