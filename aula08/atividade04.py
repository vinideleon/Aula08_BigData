#Desenvolva um algoritmo que solicite ao usuario 15 numeros inteiros e armazene-os. Ao final, apresente os numeros informados, sem repetir os valores duplicados, caso existam.

numeros = set()

for i in range(15):
    numero = int(input('informe o numero: '))
    numeros.add(numero)
print(numeros)