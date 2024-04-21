def solicitar_nombre():
    while True:
        nombre = input("Por favor, ingresa tu nombre: ")
        if nombre.isalpha():
            return nombre
        else:
            print("El nombre solo puede contener letras. Inténtalo de nuevo.")

def solicitar_edad():
    while True:
        edad_str = input("Por favor, ingresa tu edad: ")
        if edad_str.isdigit():
            return int(edad_str)
        else:
            print("La edad debe ser un número entero. Inténtalo de nuevo.")

def main():
    nombre = solicitar_nombre()
    edad = solicitar_edad()

    print(f"¡Hola {nombre}! Tienes {edad} años.")

if __name__ == "__main__":
    main()
