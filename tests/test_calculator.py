from calculator import __version__
from calculator.main import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(2, 3) == 2 / 3
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1

def test_divide_by_zero():
    try:
        divide(1, 0)
    except ValueError as e:
        assert str(e) == 'Cannot divide by zero!'
    else:
        assert False




def test_version():
    assert __version__ == '0.1.0'
