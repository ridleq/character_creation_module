from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет сумму."""
    if your_number <= 0:
        return
    abc = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {abc}')


calc(25.5)
