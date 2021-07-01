# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
     dist1 = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
     dist2 = ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) ** 0.5
     dist3 = ((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2) ** 0.5
     if (dist1 + dist2) > dist3 and (dist2 + dist3) > dist1 and (dist3 +dist1) > dist2:
         return "yes"
     return "no"
print(can_triangle((10, 12), (14, 18), (12, 12)))

# Пример вызова функции
can_triangle((10, 12), (14, 18), (12, 12))

# Не забудьте протестировать вашу функцию
