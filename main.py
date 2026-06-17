import pytest
import math
from test_eq import calculate_y

def test_valid_positive_numbers():
    # просто обычные адекватные циферки
    # a = 2, b = 6
    # y = (2*6)/(2-6) + sqrt(6-2) = 12/(-4) + sqrt(4) = -3 + 2 = -1.0
    assert calculate_y(2, 6) == -1.0

def test_valid_boundary_root_zero():
    # gjlrjhtyyjt hfdyj 0 (b == a + 0)
    # т.к. a не должно быть равно b, то b - a == 0 (ZeroDivisionError)
    # b чуть больше a, чтобы корень был почти 0
    # a = 1, b = 2 -> (1*2)/(1-2) + sqrt(2-1) = -2 + 1 = -1.0
    assert calculate_y(1, 2) == -1.0

def test_valid_floats():
    # дробные чиселки
    res = calculate_y(0.5, 4.5)
    expected = (0.5 * 4.5) / (0.5 - 4.5) + math.sqrt(4.5 - 0.5)
    assert math.isclose(res, expected)

def test_zero_division_exception():
    # деление на ноль
    with pytest.raises(ZeroDivisionError) as exc_info:
        calculate_y(5, 5)
    assert "Деление на ноль" in str(exc_info.value)

def test_negative_root_exception():
    # отрицательный корень
    with pytest.raises(ValueError) as exc_info:
        calculate_y(10, 5)
    assert "Квадратный корень из отрицательного числа" in str(exc_info.value)

@pytest.mark.parametrize("a, b, expected", [
    (0, 4, 2.0),       # проверка с нулем: (0*4)/(0-4) + sqrt(4-0) = 0 + 2 = 2.0
    (-2, -1, 3.0),     # проверка с отрицательными: (-2*-1)/(-2 - -1) + sqrt(-1 - -2) = 2/(-1) + 1 = -1.0
])
def test_parameterized_cases(a, b, expected):
    # разные знаки
    # Для теста (-2, -1) ожидаемый результат: 2 / -1 + sqrt(1) = -2 + 1 = -1
    if a == -2 and b == -1:
        expected = -1.0
    assert math.isclose(calculate_y(a, b), expected)

def test_string_input_exception():
    # ввод строки, а не чиселок
    # TypeError, т.к. строки нельзя перемножать/вычитать с числами
    with pytest.raises(TypeError):
        calculate_y("пять", 5)
        
    with pytest.raises(TypeError):
        calculate_y(5, "10")  # даже если в строке число, тип данных неверный

def test_none_input_exception():
    # передача None
    with pytest.raises(TypeError):
        calculate_y(None, 5)

@pytest.mark.parametrize("invalid_a, invalid_b", [
    ([1, 2], 5),       # список вместо числа
    (5, {'b': 10}),    # словарь вместо числа
    (True, False),     # Bool по приколу
])
def test_invalid_types_parameterized(invalid_a, invalid_b):
    # ввод разных левых штучек
    with pytest.raises(TypeError):
        # переданы типы, которые не поддерживают вычитание/умножение друг с другом
        calculate_y(invalid_a, invalid_b)

if __name__ == "__main__":
    pytest.main(["-v"])