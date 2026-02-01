import Utils

def test_add_numbers():
    assert Utils.add(5, 3) == 8

def test_subtract_numbers():
    assert Utils.subtract(10, 4) == 6

def test_multiply_numbers():
    assert Utils.multiply(7, 6) == 42

def test_divide_numbers():
    assert Utils.divide(20, 5) == 4

# Intentional error for demonstration

def test_power_numbers():
    assert Utils.power(2, 3) == 100

def dictionary_example():
    return {"name": "Karan", "age": 30, "city": "New York"}