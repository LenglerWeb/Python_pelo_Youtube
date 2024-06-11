frase = "O rato roeu a roupa do rei de Roma."

tamanho = len(frase)

cont = 0

nova_frase = ''

while cont < tamanho:

    if frase[cont] == 'r':
        nova_frase = nova_frase + frase[cont].upper()
    else:
        nova_frase = nova_frase + frase[cont]
        
    cont += 1

print(nova_frase)