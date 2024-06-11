# if, else e elif:

if False:
    print("É falso")
elif False:
    print("É falso tbm")
elif True:
    print("Este é o segundo elif e é verdadeiro")
else:
    print("Else final")

# Operadores relacionais:
# == ,  > , < , >= , <= e !=

nome = input("Seu nome: ")
idade = int(input("Sua idade: "))


idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar um empréstimo")
else:
    print(f"{nome} não pode pegar um empréstimo")


# Operadores lógicos
# and , or , not , in e not in

if 'u' in nome:
    print("Seu nome tem a letra 'U'")
else:
    print("Seu nome não tem a letra 'U'")

if 'Eduardo' not in nome:
    print("Executado o primeiro print")
else:
    print("Executado o print do ELSE")

if 'ard' not in nome:
    print("Executado o primeiro print, pq não tem 'asd' no seu nome")
else:
    print("Executado o print do ELSE, pq tem em seu nome 'ard'")

nome_db = 'Eduardo'
senha_db = 123456
senha = int(input('Digite a sua senha: '))
if nome == nome_db and senha == senha_db:
    print('Usuário logado!')
else:
    print('Usuário ou senha inválida!')