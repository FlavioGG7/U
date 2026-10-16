if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print ("Menu de opciones:")
    print ("1. Convertir a Fahrenheit")
    print ("2. Convertir a Kelvin")
    opcion = input("Seleccione una opción (1 o 2): ")
    match opcion:
        case "1":
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
        case "2":
            kelvin = celsius + 273.15
            print(f"{celsius} grados Celsius son {kelvin} grados Kelvin.")
        case _:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            