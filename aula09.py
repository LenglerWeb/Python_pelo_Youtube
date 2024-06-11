# Iterando strings com WHILE em Python

print("Primeiro exemplo: \n")
frase = "o rato roeu a roupa do rei de Roma."

tamanho = len(frase)
print(f"A quantidade de letras na frase: {tamanho}")
print(f"Frase invertida: > {frase[::-1]}")

# Outro exemplo:
print("\nSegundo exemplo: \n")

cont = 0

nova_frase = ''

while cont < tamanho:

    if frase[cont] == 'r':
        nova_frase = nova_frase + frase[cont].upper()
    else:
        nova_frase = nova_frase + frase[cont]
        
    cont += 1

print(f'A frase com todos os "r" em maiúsculo: > {nova_frase}')


# Outro exemplo:
print("\nTerceiro exemplo: \n")

c = 0
contagem = 0
letra = ''

while c < tamanho:
    conta = frase.count(frase[c])

    if contagem < conta and frase[c].strip():
        letra = frase[c]
        contagem = conta

    #print(frase[c], conta)

    c += 1

print(letra, contagem)