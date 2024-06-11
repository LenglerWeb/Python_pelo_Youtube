"""
Exemplo de posição de indices:

indices positivos  [012345678]
texto =             Python s2
indices negativos -[987654321]
"""


texto = "Python_s2"
print(texto[4])
print(texto[2:6])
print(texto[7:])
print(texto[:6])
print(texto[-1])
print(texto[-9])
print(texto[-9:-3])
print(texto[:-1])

url = "www.teraa.com.br/"
print(len(url))
print(url[:-1])
print(url[0::2])
print(url[0:10:2])