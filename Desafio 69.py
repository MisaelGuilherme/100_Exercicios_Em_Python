print('====== DESAFIO 69 ======')
contIdade = 0
contSexoM = 0
contMulher = 0
while True:
    sexo = input('Digite o Sexo [F/M]: ').upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite o Sexo [F/M]: ')
    idade = int(input('Digite a Idade: '))
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contSexoM += 1
    if sexo == 'F' and idade < 20:
        contMulher += 1
    parada = str(input('Deseja continuar: [S/N]')).upper()
    while parada != 'S' and parada != 'N':
        parada = str(input('Deseja continuar: [S/N]'))
    if parada == 'N':
        break
    print('')
print('')
print(f'Pessoas Maiores de 18 anos: {contIdade}')
print(f'Homens Cadastrados: {contSexoM}')
print(f'Mulheres Com Menos de 20 anos: {contMulher}')