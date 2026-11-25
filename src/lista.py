
def estaEnRango(valor, minimo, maximo):
    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False

def estaEnLista(valor, lista):
    if valor in lista:
        return True
    else:
        return False

def main():
    lista = [6, 14, 11, 3, 2, 1, 15, 19]

    numero = int(input("Introduce un número del 1 al 20: "))

    if estaEnRango(numero, 1, 20):
        print("El número está dentro del rango.")

        if estaEnLista(numero, lista):
            print("El número está en la lista.")
        else:
            print("El número no está en la lista.")
    else:
        print("El número está fuera del rango.")

if __name__ == "__main__":
    main()
