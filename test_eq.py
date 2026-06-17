import math

def calculate_y(a: float, b: float) -> float:
    # деление на 0
    if a == b:
        raise ZeroDivisionError("Деление на ноль: переменные 'a' и 'b' не должны быть равны")
    
    # отрицательный корень
    if b < a:
        raise ValueError("Квадратный корень из отрицательного числа: 'b' должно быть больше или равно 'a'")
    return (a * b) / (a - b) + math.sqrt(b - a)

def main():
    print("y = (a * b) / (a - b) + sqrt(b - a)") 
    try:
        # ввод некорректных данных (не циферки)
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        
        # ну типа считает вроде
        result = calculate_y(a, b)
        print(f"Результат y = {result:.4f}")
        
    except ValueError as e:
        # ошибки перевода строки в циферки, так и ошибку из функции
        if "Квадратный корень" in str(e):
            print(f"Математическая ошибка: {e}")
        else:
            print("Ошибка ввода: введите корректные числовые значения")
            
    except ZeroDivisionError as e:
        # ошибка равенства чисел a и b (деление на 0)
        print(f"Математическая ошибка: {e}")
        
    except Exception as e:
        # ну мало ли еще чего сломается
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
