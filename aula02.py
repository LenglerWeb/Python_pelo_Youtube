print("Aspas \"isso está dentro de aspas\" duplas,", 'Aspas simples')
print('Aspas "isso está dentro de aspas duplas" simples')
print("Se quiser usar 'aspas simples' dentro de aspas duplas, não tem problema.")
a = '5' + 'A4'
print(a)

if True:
    a = 2
    print(a)
    a = a +1
    a = a


# Variáveis

nome = "Eduardo Lengler"
idade = 46
peso = 80
altura = 1.73

imc = peso / (altura**2)
print("{n} tem {i} anos e pesa {p} quilos. Seu IMC é {im}. {n}, tome cuidado com a sua saúde!".format(n=nome, i=idade, p=peso, im=imc))

# agora usando números dos índices de cada variável:
print("{0} tem {1} anos e pesa {2} quilos. Seu IMC é {3}. {0}, tome cuidado com a sua saúde!".format(nome, idade, peso, imc))

# Melhor método para usar com print()
print(f'{nome} tem {idade} anos e pesa {peso} quilos. Seu IMC é {imc}. {nome}, tome cuidado com a sua saúde!')

# Outra forma de mostrar uma mensagem usando uma variável que depois é mostrada com o print()
mensagem = f'''
Esse é uma mensagem
gigante e que aqui e
agora eu vou exibir 
as mensagem as variáveis.
Variável nome = {nome}
Variavel idade = {idade} anos.
'''
print(mensagem)

'''Para concatenar valores de tipos diferentes, é necessário fazer um cast (conversão)
dos valores. É possível realizar operações aritméticas entre Int e Float:
'''

inteiro = 5
real = 6.2
booleano = True
texto = "9.5"

variavel = 10 > 2

print( inteiro + real)
print(inteiro + float(texto))
float_texto = float(texto)
print(float_texto + real)
print(int(float(texto)))
print(variavel)

print("O tipo original da variável inteiro é: ", type(inteiro))
inteiro = str(inteiro)
print("O Tipo modificado da variável inteiro agora é: ", type(inteiro))