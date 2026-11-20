produtos = []

for i in range(5):
    produto = input('informe o nome do produto: ')
    produtos.append(produto)  #adiciona na lista produtos

print(produtos)

#acesse ao elemento
n= int(input('digite o indice do elemento a acessar: '))
print(produtos[n-1]) # 1


# Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f'informe o novo nome do produto {n}: ') # 2
print(produtos)

# Remover da lista
produto_a_remover = input('\ndigite o nome do produto a remover: ')
if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)

# pesquisar os metodos insert, pop(), clear 