if __name__ == "__main__":
    Pesos = float(input("Ingrese la cantidad en Pesos mexicanos: "))
    print ("Menu de opciones:")
    print ("1. Convertir a Dolares (USD) 1 USD = 18.5 MXN")
    print ("2. Convertir a Euros (EUR) 1 EUR = 20.0 MXN")
    print ("3. Convertir a Bahts (THB) 1 THB = 0.5 MXN")
    print ("4. Convertir a Yenes (JPY) 1 JPY = 0.12 MXN")
    print ("5. Convertir a won surcoreano (KRW) 1 KRW = 0.014 MXN")
    print ("6. Convertir a dolares australianos (AUD) 1 AUD = 12.7 MXN")
    print ("7. Convertir a soles peruanos (PEN) 1 PEN = 5.0 MXN")
    print ("8. Convertir a dolares canadienses (CAD) 1 CAD = 13.0 MXN")
    print ("9. Convertir a bolivares (VES) 1 VES = 0.020 MXN")
    print ("10. Convertir a pesos argentinos (ARS) 1 ARS = 0.012 MXN")
    opcion = input("Seleccione una opción (1 a 10): ")
    match opcion:
        case "1":
            dolares = Pesos / 18.5
            print(f"{Pesos} Pesos mexicanos son {dolares:.2f} Dolares (USD)")
        case "2":
            euros = Pesos / 20.0
            print(f"{Pesos} Pesos mexicanos son {euros:.2f} Euros (EUR)")
        case "3":
            bahts = Pesos / 0.5
            print(f"{Pesos} Pesos mexicanos son {bahts:.2f} Bahts (THB)")
        case "4":
            yenes = Pesos / 0.12
            print(f"{Pesos} Pesos mexicanos son {yenes:.2f} Yenes (JPY)")
        case "5":
            won = Pesos / 0.014
            print(f"{Pesos} Pesos mexicanos son {won:.2f} Won surcoreano (KRW)")
        case "6":
            aud = Pesos / 12.7
            print(f"{Pesos} Pesos mexicanos son {aud:.2f} Dolares australianos (AUD)")
        case "7":
            soles = Pesos / 5.0
            print(f"{Pesos} Pesos mexicanos son {soles:.2f} Soles peruanos (PEN)")
        case "8":
            cad = Pesos / 13.0
            print(f"{Pesos} Pesos mexicanos son {cad:.2f} Dolares canadienses (CAD)")
        case "9":
            bolivares = Pesos / 0.020
            print(f"{Pesos} Pesos mexicanos son {bolivares:.2f} Bolivares (VES)")
        case "10":
            ars = Pesos / 0.012
            print(f"{Pesos} Pesos mexicanos son {ars:.2f} Pesos argentinos (ARS)")
        case _:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 10.")
            