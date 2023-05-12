def collatz(numero):
    sucesion = []
    numero_introducido = numero
    while numero != 1:
        sucesion.append(numero)
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = (numero * 3) + 1
    sucesion.append(1)
    return f'La sucesión del número {numero_introducido} es: {sucesion}'

