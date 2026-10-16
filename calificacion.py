if __name__ == "__main__":
    Parciales = float(input("Ingresa tu calificacion total de parciales: "))
    if Parciales < 0 or Parciales > 100:
        print("Calificacion invalida")
    else:
        print("Calificacion valida")
        Proyecto = float(input("Ingresa tu calificacion total de proyecto: "))
        if Proyecto <=0:
            print("Calificacion invalida")
        else:
            print("Calificacion valida")
            Examen_final = float  (input("Ingresa tu calificacion total de examen final: "))
            if Examen_final <= 0:
                print("Calificacion invalida")
            else:
                print("Calificacion valida")
                Calificacion_final = (Parciales * 0.4) + (Proyecto * 0.3) + (Examen_final * 0.3)
                print("Tu calificacion final es: ", Calificacion_final)
                