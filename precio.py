if __name__ == "__main__":
    precio = float(input("Ingresa el precio del producto: "))
    if precio < 0:
        print("Precio invalido")
    elif precio <= 100:
        print("Sin descuento, Total a pagar: ", precio)
    elif precio <= 200:
        descuento = precio * 0.10
        print("Descuento del 10%, Total a pagar: ", precio - descuento)
    elif precio <= 500:
        descuento = precio * 0.20
        print("Descuento del 20%, Total a pagar: ", precio - descuento)
    elif precio > 500:
                descuento = precio * 0.25
                print("Descuento del 25%, Total a pagar: ", precio - descuento)
        