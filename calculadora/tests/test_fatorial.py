import pytest

from app.fatorial import fatorial

def test_fatorial_positivo():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-5)

def test_fatorial_decimal():
    with pytest.raises(TypeError):
        fatorial(5.5)