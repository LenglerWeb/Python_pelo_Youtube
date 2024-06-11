"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, min, max
range
"""

texto = "Valor"
lista = ['A', 'B', 'C', 'D', 'E']
print(lista[-5])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1])

print("\n Novo exemplo: ")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8, 9, 10]

print(lista1)
print(lista2)

lista1.extend(lista2)
print(lista1)

# Adicionando a letra "a" na lista1:
lista1.extend('a')
print(lista1)

# Adicionando a letra "b" no final da lista2:
lista2.append('b')
print(lista2)
# Adicionando a palavra "Banana" no início da lista2:
lista2.insert(0, "Banana")
print(lista2)
lista2.pop(0)

# Removendo a letra "b" do final da lista2:
lista2.pop()
print(lista2)

# Removendo o item que está no índice 1 da lista2:
lista2.pop(1)
print(lista2)

# Excluir uma sequencia de itens dentro da lista2:
del(lista2[3:6])
print(lista2)

# Mostrar os valores máximos e mínimos dentro da lista2:
print( min(lista2) )
print( max(lista2) )

# Criar uma lista de elementos nova usando range():
lista3 = list(range(1, 11))
print(lista3)

lista4 = list(range(0, 100, 10))
print(lista4)


