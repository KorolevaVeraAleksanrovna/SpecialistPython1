# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

x = int(input("Введите номер месяца: "))
if x==12 or 1<=x<=2:
    print("Winter")
elif 3<=x<6:
    print("Spring")
elif 6<=x<9:
    print("Summer")
elif 9<=x<12:
    print("Autumn")
