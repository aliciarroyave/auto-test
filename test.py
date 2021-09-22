def suma(a, b):
    return a + b


def test_suma():
    assert suma(2, 3) == 5
    assert suma('gat', 'ito') == 'gatito'


def resta(a, b):
    return a + b  #intencional sera solucionado luego

def test_subtract():
    assert subtract(2, 3) == -1