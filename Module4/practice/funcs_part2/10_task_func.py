# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    n = len(args)
    sum_args = 0
    for el in args:
        sum_args = sum_args + el
    average = sum_args/len(args)
    return average
    pass

print(round(average(3, -5, 25), 2))
print(round(average(3, 4, 8), 2))
print(round(average(1, 4, 5, -3, 8, 4), 2))
print(round(average(-10, 12, 6.3, -5.5, 7, 0.2), 2))
