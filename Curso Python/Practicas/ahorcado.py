
import random

def obtener_palabra():
    palabras = ["botafumeiro", "boniato", "juja", "bombisima", "poto", "pazguato"]
    return palabras[random.randint(0, len(palabras) - 1)]

#def obtener_palabra():
#   palabras = ["botafumeiro", "boniato", "juja", "bombisima", "poto", "pazguato"]
#  return random.choice(palabras)



def juego():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 10
    final = False

    print("Bienvenido al ahorcado")
    print(f"Tienes {intentos} intentos")
    print(progreso(palabra, letras_adivinadas))

    while not final:
        # Solicitar entrada del usuario y validarla
        dicho = input("Introduce una letra: ").lower()

        # Validar que sea una sola letra
        if len(dicho) != 1 or not dicho.isalpha():
            print("Por favor, introduce **solo una letra válida**.")
            continue

        # Verificar si la letra ya se ha intentado
        if dicho in letras_adivinadas:
            print("Ya intentaste esa letra, elige otra.")
            continue

        # Agregar la letra a las letras adivinadas
        letras_adivinadas.append(dicho)

        # Verificar si la letra está en la palabra
        if dicho in palabra:
            print(f"¡Bien! La letra '{dicho}' está en la palabra.")
        else:
            intentos -= 1
            print(f"La letra '{dicho}' no está en la palabra. Te quedan {intentos} intentos.")

        # Mostrar el progreso
        print(progreso(palabra, letras_adivinadas))

        # Verificar si el usuario ganó o perdió
        if set(palabra) <= set(letras_adivinadas):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
            final = True
        elif intentos <= 0:
            print(f"Lo siento, has perdido. La palabra era: {palabra}")
            final = True



def progreso(palabra, letras):
    adivinado = ""
    for letra in palabra:
        if letra in letras:  # Si la letra ha sido adivinada
            adivinado += letra
        else:  # Si no ha sido adivinada
            adivinado += "_"
    return adivinado



juego()




