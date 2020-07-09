print('====== DESAFIO 53 ======')
phrase = str(input('Digite uma frase: ')).strip().split()
junto = ''.join(phrase)
cont = len(junto)
recebe = ''
for letra in range(cont-1, -1, -1):
    recebe = recebe + junto[letra]
if recebe == junto:
    print(recebe)
    print(f'A frase: {junto} é um palíndromo!' )
else:
    print(recebe)
    print(f'A frase: {junto} não é um palindromo!')