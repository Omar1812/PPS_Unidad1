def esBinario(strbinario):
    if strbinario == "":
        return False

    for digito in strbinario:
        if digito != "0" and digito != "1":
            return False

    return True

def main():
    numero = input("Introduce un número binario: ")

    if esBinario(numero):
        decimal = int(numero, 2)
        print("El número en decimal es:", decimal)
    else:
        print("El número introducido no es binario")

if __name__ == "__main__":
    main()