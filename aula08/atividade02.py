# Desenvolva um algoritmo que permita ao usuario informar numeros inteiros ate que digite a letra N para encerrar. Os numeros informados deverão ser armazenados em uma lista. Ao final, apresente a quantidade de numeros armazenados.

numeros = []
resposta = 'S'

while resposta == 'S':
    numero = int(input('informe os numeros: '))
    numeros.append(numero)
    print(numeros)
    resposta = input('\nquer continuar? [S/N]').upper()

quantidade = len(numeros)

print(f'Tem um total de {quantidade} armazenados \nPrograma encerrado')