#desenvolva um algoritmo que solicite ao usuario 12 numeros inteiros, armazene-os em uma lista e apresente todos os numeros informados em ordem crescente.

numeros = []

for i in range(12):
    numero = int(input('informe o numero: '))
    numeros.append(numero)
print(numeros)

ordenada = sorted(numeros)
print(ordenada)