# tests/test_binario.py
import unittest

# Importamos las funciones desde la carpeta src
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista

class TestPracticaUnidad1(unittest.TestCase):
    """
    Suite de pruebas unitarias con unittest para comprobar 
    las funciones de binario, rango y listas de forma básica.
    """

    def test_es_binario_valido(self):
        # Comprobamos cadenas binarias correctas
        self.assertTrue(esBinario("1001"))
        self.assertTrue(esBinario("0"))
        self.assertTrue(esBinario("11110000"))

    def test_es_binario_invalido(self):
        # Comprobamos cadenas no binarias o erróneas
        self.assertFalse(esBinario("1002"))
        self.assertFalse(esBinario("Hola"))
        self.assertFalse(esBinario(""))

    def test_esta_en_rango_valido(self):
        # Comprobamos valores dentro del rango o en los límites
        self.assertTrue(estaEnRango(5, 1, 20))
        self.assertTrue(estaEnRango(1, 1, 20))   # Límite inferior
        self.assertTrue(estaEnRango(20, 1, 20))  # Límite superior

    def test_esta_en_rango_invalido(self):
        # Comprobamos valores fuera del rango
        self.assertFalse(estaEnRango(0, 1, 20))
        self.assertFalse(estaEnRango(21, 1, 20))

    def test_esta_en_lista_positivo(self):
        # Comprobamos valores que SÍ están en la lista del libro
        lista_ejemplo = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertTrue(estaEnLista(14, lista_ejemplo))
        self.assertTrue(estaEnLista(1, lista_ejemplo))

    def test_esta_en_lista_negativo(self):
        # Comprobamos valores que NO están en la lista
        lista_ejemplo = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertFalse(estaEnLista(10, lista_ejemplo))
        self.assertFalse(estaEnLista(99, lista_ejemplo))

if __name__ == "__main__":
    unittest.main()