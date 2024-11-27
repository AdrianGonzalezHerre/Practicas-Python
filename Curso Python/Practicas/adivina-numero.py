
import random


def adivina():
    numero = random.randint(1, 101)
    intentos = 0
    adivinado = False
    print("Bienvenido al juego\nIntenta adivinar el número")

    while not adivinado:
        try:
            x = int(input("Introduce un número entre el 1 y el 100: "))
            while x > 100 or x < 1:
                x = int(input("Has introducido un número fuera de rango\nInténtalo de nuevo: "))
            intentos += 1
            if numero > x:
                print(f"El número que quieres adivinar es mayor que {x}")
            elif numero < x:
                print(f"El número que quieres adivinar es menor que {x}")
            else:
                print(f"¡Felicidades, adivinaste el número en {intentos} intentos!")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un número válido.")

            
adivina()
