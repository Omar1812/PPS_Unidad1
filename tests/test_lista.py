# tests/test_lista.py
import pytest

# Importamos las funciones desde la carpeta src
from src.binario import esBinario
from src.lista import estaEnRango, estaEnLista


def test_esBinario():
    # Casos válidos
    assert esBinario("1001") == True
    assert esBinario("0") == True
    
    # Casos inválidos
    assert esBinario("1002") == False
    assert esBinario("Hola") == False
    assert esBinario("") == False


def test_estaEnRango():
    # Dentro del rango y límites
    assert estaEnRango(5, 1, 20) == True
    assert estaEnRango(1, 1, 20) == True
    assert estaEnRango(20, 1, 20) == True
    
    # Fuera del rango
    assert estaEnRango(0, 1, 20) == False
    assert estaEnRango(25, 1, 20) == False


def test_estaEnLista():
    lista_ejemplo = [6, 14, 11, 3, 2, 1, 15, 19]
    
    # Valores que SÍ están
    assert estaEnLista(14, lista_ejemplo) == True
    assert estaEnLista(1, lista_ejemplo) == True
    
    # Valores que NO están
    assert estaEnLista(10, lista_ejemplo) == False
    assert estaEnLista(99, lista_ejemplo) == False