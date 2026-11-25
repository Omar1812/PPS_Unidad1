# src/lista.py

def estaEnRango(valor, minimo, maximo):
    """
    Devuelve True o False determinando si el valor se encuentra 
    entre el mínimo y el máximo (inclusive).
    """
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    """
    Devuelve True o False determinando si el valor está en la lista.
    """
    return valor in lista


def main():
    print("=== PROGRAMA DE VALIDACIÓN DE RANGO Y LISTA ===")
    
    # Definimos la lista que exige el ejercicio del libro
    lista_objetivo = [6, 14, 11, 3, 2, 1, 15, 19]
    
    try:
        # 1. Pedimos un número entero al usuario
        entrada = int(input("Introduce un número entero del 1 al 20: "))
        
        # 2. Comprobamos si está en el rango correcto (1 y 20) usando la función
        if estaEnRango(entrada, 1, 20):
            print(f"-> El número {entrada} está dentro del rango permitido (1 al 20).")
            
            # 3. Comprobamos si está en la lista usando la otra función
            if estaEnLista(entrada, lista_objetivo):
                print(f"-> ¡Enhorabuena! El número {entrada} SÍ está dentro de la lista {lista_objetivo}.")
            else:
                print(f"-> El número {entrada} NO se encuentra en la lista.")
        else:
            print(f"-> Error: El número {entrada} está fuera del rango (debe ser entre 1 y 20).")
            
    except ValueError:
        print("-> Error: Debes introducir obligatoriamente un número entero válido.")

if __name__ == "__main__":
    main()