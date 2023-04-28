import pytest
from optimizar import Optimizar

def test_media():
    optimizado = Optimizar()
    optimizado.array.clear()
    assert len(optimizado.array) == 0
    optimizado.add(5)
    optimizado.add(4)
    optimizado.add(3)
    assert len(optimizado.array) == 3
    assert optimizado.media() == 4.0

def test_add():
    optimizado = Optimizar()
    optimizado.add(6)
    assert optimizado.array == [5,4,3,6]
    
