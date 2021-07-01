# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def can_triangle(p1, p2, p3):
    dist1 = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    dist2 = ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) ** 0.5
    dist3 = ((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2) ** 0.5
    if (dist1 + dist2) > dist3 and (dist2 + dist3) > dist1 and (dist3 + dist1) > dist2:
        perim = dist1 + dist2 + dist3
        p = perim/2
        s = (p*(p - dist1)*(p - dist2)*(p - dist3))**0.5
        return p, s
    return False
print(can_triangle((1, 1), (1, 4), (5, 1)))
print(can_triangle((1, 1), (1, 3), (1, 4)))
print(can_triangle((1, 1), (3, 4), (5, 3)))


# Не забудьте протестировать вашу функцию
