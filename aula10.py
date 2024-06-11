"""
FOR in em Python
Iterando strings com FOR
Função range(start=0, stop, step=1)
"""

texto = 'Python'

print("Palavra 'Python' escrita com WHILE:")
c = 0
while c < len(texto):
    print(texto[c])
    c += 1

print("\n")

print("Palavra 'Python' escrita com FOR:")
for n, letra in enumerate(texto):
    print(f'O índice [{n}], referente a letra: {letra}')


print("\n")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lista[-1])
print(lista[::-1])


print("\n")
print("Palavra 'Python' escrita usando FOR e colocando em maiúsculas as letras 't e h':")
novo_texto = ''
for letra in texto:
    if letra == 't':
        novo_texto = novo_texto + letra.upper()
    elif letra == 'h':
        novo_texto += letra.upper()
    else:
        novo_texto += letra

print(novo_texto)