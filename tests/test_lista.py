
import pytest

from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista


def test_esBinario():
    assert esBinario("1001") == True
    assert esBinario("0") == True
    assert esBinario("1002") == False
    assert esBinario("Hola") == False
    assert esBinario("") == False


def test_estaEnRango():
    assert estaEnRango(5, 1, 20) == True
    assert estaEnRango(1, 1, 20) == True
    assert estaEnRango(20, 1, 20) == True
    assert estaEnRango(0, 1, 20) == False
    assert estaEnRango(25, 1, 20) == False


def test_estaEnLista():
    lista = [6, 14, 11, 3, 2, 1, 15, 19]

    assert estaEnLista(14, lista) == True
    assert estaEnLista(1, lista) == True
    assert estaEnLista(10, lista) == False
    assert estaEnLista(99, lista) == False
