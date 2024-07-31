def factorial(n):
    """
    Функція для обчислення факторіалу числа.

    Параметри:
    - n (int): Ціле число, для якого обчислюється факторіал.

    Повертає:
    int: Факторіал введеного числа.
    """
    if n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Приклад використання функції:
number = 5
result = factorial(number)
print(f"Факторіал числа {number} дорівнює {result}")
