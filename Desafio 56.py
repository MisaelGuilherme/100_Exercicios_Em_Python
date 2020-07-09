print('====== DESAFIO 56 ======')
soma = 0
num = 0
quant = 0
for c in range(1,5):
    nome = str(input(f'Digite o {c}º nome: ')).capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M][F]: ')).strip().upper()
#-------- soma de todas as idades --------
    soma += idade
#-------- verificação de homem mais velho -------
    if c == 1 and sexo == 'M':
        num = idade
    if sexo == 'M' and idade > num:
        num = idade
        maisVelho = nome
    if sexo == 'F' and idade < 20:
        quant += 1
#------- calculo da média de todas idades ------
media = soma/c+1
#------- mostrando na tela os resultados ---------
print(f'A média de idade é: {media:.2f}')
print(f'O homem mais velho é: {maisVelho} com {num} anos')
print(f'A quantidade de mulher abaixo de 20 anos é: {quant}')