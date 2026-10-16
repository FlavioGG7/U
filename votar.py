if __name__ == "__main__":
    edad = int(input("Ingresa tu edad: "))
    if edad < 0 or edad > 100:
        print("Edad invalida")
    elif edad >= 18:
        print("Eres mayor de edad y puedes votar")
    else:
        print("Eres menor de edad y no puedes votar")
        