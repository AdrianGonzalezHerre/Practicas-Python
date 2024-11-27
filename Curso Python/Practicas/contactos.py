

def menu():
    print("Agenda de Contactos\n1. Agregar contacto\n2.Eliminar contacto\n3. Buscar contacto\n4. Lista de contactos\n5. Salir")

def agregar(agenda):
    nombre = input("Introduzca el nombre del contacto ")
    telefono = input("Introduce su numero ")
    email = input("Introduce el correo electronico ")
    agenda[nombre] = {
        "telefono":telefono,
        "email" : email
    }
    print(f"Se ha añadido {nombre} correctamente")

def eliminar(agenda):
    """Eliminar un contacto de la agenda."""
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")

def buscar(agenda):
    """Buscar un contacto en la agenda."""
    nombre = input("Introduce el nombre del contacto que deseas buscar: ").strip()
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")

def listar(agenda):
    """Listar todos los contactos de la agenda."""
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\n--- Lista de Contactos ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
        print("--------------------------")


def agenda():
    agenda={}
    while True:
        menu()
        opcion = (input("Introduce un numero del menu: "))
        numero = int(opcion)
        if not opcion.isdigit() or int(opcion) not in range(1, 6):
            print("Por favor, introduce un número válido entre 1 y 5.")
            continue
        elif numero == 1:
             print("Ha accedido a Agregar contacto")
             agregar(agenda)
        elif numero == 2:
             print("Ha accedido a Eliminar contacto")
        elif numero == 3:
             print("Ha accedido a Buscar contactos")
        elif numero == 4:
             print("Ha accedido a Lista de contactos")
        elif numero == 5:
            print("Gracias por utilizar nuestro sistema")
            break


agenda()
        