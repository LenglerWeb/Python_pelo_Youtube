x = 0

while x < 10:
    if x == 3:
        x += 1
        #break
        continue

    print(x)
    x += 1

print("Abacou o exemplo 1!")


i = 0
j = 1

while i < 5:

    while j <= 5:
        print(f'O "i" vale {i} e o "j" vale {j}')
        j += 1
    i += 1
print("Abacou o exemplo 2!")

a = 0
while a < 10:
    b = 0
    while b <= 5:
        print(f'({a},{b})')
        b += 1
    a += 1

print("Abacou o exemplo 3!")

sair = 'n'
while sair == 'n':
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um número inteiro: "))
    operador = input("Digite um operador: ('+' , '-' , '*' , '/'): ")
    
    
    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        if operador != "+" or "-" or "*" or "/":
            break
        


print("Abacou o exemplo 4!")