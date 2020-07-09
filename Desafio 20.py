from random import shuffle
print('====== DESAFIO 20 ======')
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluino: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('O nome escolhido é: ', lista)
