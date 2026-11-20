# uma empresa esta registrando os valores de 10 vendas realizadas durante o dia. desenvolva um algoritmo que solicite ao usuario os 10 valores, armazene-os em uma lista e apresente a soma total das vendas. 
vendas = []

for i in range(10):
    venda = float(input('informe os valores da sua venda: '))
    vendas.append(venda)
print(vendas)

total = sum(vendas)
print(total)

