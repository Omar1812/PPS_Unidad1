def esBinario(strbinario):
    """
    Función que comprueba si una cadena de texto es un número binario válido.
    Devuelve True si solo tiene '0' o '1', y False en caso contrario.
    """
    # Si lo que nos pasan no es texto (str) o está vacío, devolvemos False
    if not isinstance(strbinario, str) or len(strbinario) == 0:
        return False
    
    # Recorremos cada letra (carácter) de la cadena
    for caracter in strbinario:
        # Si encontramos algo que no sea '0' o '1', no es binario
        if caracter not in '01':
            return False
            
    # Si ha pasado todo el bucle sin fallar, es un binario válido
    return True


def main():
    print("=== PROGRAMA PARA COMPROBAR Y CONVERTIR BINARIO ===")
    
    # 1. Pedimos un número binario al usuario por teclado
    entrada = input("Introduce un número binario (ej. 1001): ")
    
    # 2. Llamamos a la función obligatoria para comprobar si es válido
    if esBinario(entrada):
        # 3. Si es válido, lo convertimos a decimal
        # La función int(cadena, 2) convierte texto en base 2 (binario) a un número decimal
        decimal = int(entrada, 2)
        print(f"-> El número binario {entrada} en formato decimal es: {decimal}")
        
    else:
        print(f"-> Error: '{entrada}' NO es una cadena binaria válida (solo debe contener 0 y 1).")


# Esto le indica a Python que ejecute la función main() cuando lancemos el fichero
if __name__ == "__main__":
    main()