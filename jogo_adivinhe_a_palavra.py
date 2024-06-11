import random 

cerca = '###########################'
print(cerca)
print("Adivinhe a palavra secreta")
print(cerca)
print()

palavra_secreta = 'aula'
letra_digitada = []
chances = 3

while True:
    if chances < 1:
        print("Você perdeu!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas UMA letra!")
        continue

    letra_digitada.append(letra)

    if letra in palavra_secreta:
        print(f'Acertou, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Errou! A letra "{letra}" NÃO EXISTE na palavra secreta.')
        letra_digitada.pop()

    
    letra_secreta_temp = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_digitada:
            letra_secreta_temp += letra_secreta
        else:
            letra_secreta_temp += "*"

    if letra_secreta_temp == palavra_secreta:
        print(f"Você ACERTOU a palavra secreta!! A palavra era {letra_secreta_temp}")
        break
    else:
        print(f"A palavra secreta está assim: {letra_secreta_temp}")

    if letra_digitada is not palavra_secreta:
        chances -= 1
    print(f"Você ainda tem {chances} de 3 tentativas!")