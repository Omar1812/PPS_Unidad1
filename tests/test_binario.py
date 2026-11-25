
import unittest

from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista


class TestPractica(unittest.TestCase):

    def test_esBinario(self):
        self.assertTrue(esBinario("1001"))
        self.assertTrue(esBinario("0"))
        self.assertFalse(esBinario("Hola"))
        self.assertFalse(esBinario("1002"))
        self.assertFalse(esBinario(""))

    def test_estaEnRango(self):
        self.assertTrue(estaEnRango(5, 1, 20))
        self.assertTrue(estaEnRango(1, 1, 20))
        self.assertTrue(estaEnRango(20, 1, 20))
        self.assertFalse(estaEnRango(0, 1, 20))
        self.assertFalse(estaEnRango(21, 1, 20))

    def test_estaEnLista(self):
        lista = [6, 14, 11, 3, 2, 1, 15, 19]

        self.assertTrue(estaEnLista(14, lista))
        self.assertTrue(estaEnLista(1, lista))
        self.assertFalse(estaEnLista(10, lista))
        self.assertFalse(estaEnLista(99, lista))


if __name__ == "__main__":
    unittest.main()
