tupla = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUARTOZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente Novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {tupla[num]}')
