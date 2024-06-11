cont = 1
acumulador = 1

while cont <= 10:
    
    print(cont, acumulador)

    if cont > 5:
        break

    acumulador = acumulador + cont
    cont += 1

else:
    cont == 11
    print(cont, acumulador)
    print("Chegou no ELSE dentro do WHILE, finalizando execução!")

print("não passou pelo laço ELSE dentro do WHILE, finalizando execução!")