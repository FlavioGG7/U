if __name__ == "__main__":
    calificacion = float(input("Ingresa tu calificacion total: "))
    if calificacion >= 90 and calificacion <= 100:
        print("Tu calificacion es A")
    elif calificacion >= 80 and calificacion <= 89:
        print("Tu calificacion es B")
    elif calificacion >= 70 and calificacion <= 79:
        print("Tu calificacion es C")
    elif calificacion >= 60 and calificacion <= 69:
        print("Tu calificacion es D")
    elif calificacion >= 0 and calificacion < 60:
        print("Tu calificacion es F")
    else:
        print("Calificacion invalida")