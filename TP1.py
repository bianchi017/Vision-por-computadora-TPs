def adivinar(cantidadIntentos):
    i = 1
    import random
    numero = random.randint(0, 100)
    while i <= cantidadIntentos:
        guess = int(input('Ingrese un número: '))
        if guess == numero:
            print('Felicitaciones, adivinaste con: ')
            print(i, 'intentos')
            break
        elif guess < numero:
            print('Pista: el número es un poco mayor')
            i += 1
        else:
            print('Pista: el número es un poco menor')
            i += 1
    else:
        print("Lo siento, has excedido el número de intentos máximos que son de: ")
        print(cantidadIntentos,'intentos')


adivinar(5)

