print('====== DESAFIO ======')
import random

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quartp aluno: ')
lista = [nome1, nome2, nome3, nome4]
print('O aluno escolhido foi: ', random.choice(lista))
