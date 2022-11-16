"""# Завдання 1
name = input("Як тебе звати? ")
print("О, ми з тобою тезки" if name.upper() == "АЛЬОНА" else "Приємно познайомитися")

# Завдання 2
from math import pi, cos
x = float(input("Введіть значення в діапазоні [-П; П] "))
if - pi <= x <= pi:
    print("y = ", cos(3 * x))
else:
    print("Значення повинно бути в діапазоні [-П; П]")"""

# Завдання 3
a = float(input("Введіть перший коефіцієнт "))
b = float(input("Введіть другий коефіцієнт "))
c = float(input("Введіть третій коефіцієнт "))
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Рівняння має безліч коренів")
elif a == 0 and b == 0:
    print("Рівняння не має жодного кореня")
elif a == 0:
    print("Рівняння має єдиний розв'язок: ", b / c)
elif d == 0:
    print("Рівняння має єдиний розв'язок: ", - b / 2 / a)
elif d < 0:
    print("Дійсних коренів немає")
else:
    print("Перший корінь рівняння: ", round((- b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a, 3))
    print("Другий корінь рівняння: ", round((- b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a, 3))

"""# Завдання 4:
from math import pi, sin, cos, tan
print("""Що хочете зробити?
1.  Додати
2.  Відняти
3.  Помножити
4.  Поділити
5.  Піднести до степені
6.  Знайти квадратний корінь
7.  Знайти кубічний корінь
8.  Знайти sin
9.  Знайти cos
10. Знайти tan""")
m = int(input("Оберіть необхідний варіант з меню: "))
if m == 1:
    a = float(input("Уведіть перше число: "))
    b = float(input("Уведіть друге число: "))
    print("Сума чисел: ", a + b)
elif m == 2:
    a = float(input("Уведіть перше число: "))
    b = float(input("Уведіть перше число: "))
    print("Різниця чисел: ", a - b)
elif m == 3:
    a = float(input("Уведіть перше число: "))
    b = float(input("Уведіть перше число: "))
    print("Добуток чисел: ", a * b)
elif m == 4:
    a = float(input("Уведіть перше число: "))
    b = float(input("Уведіть перше число: "))
    print("Відношення чисел: ", round(a / b), 3)
elif m == 5:
    a = float(input("Уведіть число: "))
    b = float(input("До якої степені піднести: "))
    print("Відповідь: ", a ** b)
elif m == 6:
    a = float(input("Уведіть число: "))
    print("Відповідь: ", a ** 0.5)
elif m == 7:
    a = float(input("Уведіть число: "))
    print("Відповідь: ", a ** (1 / 3))
elif m == 8:
    a = float(input("Уведіть число: "))
    print("sin(", round(a), ") = ", round(sin(a), 3))
elif m == 9:
    a = float(input("Уведіть число: "))
    print("cos(", round(a), ") = ", round(cos(a), 3))
elif m == 10:
    a = float(input("Уведіть число: "))
    print("tan(", round(a), ") = ", round(tan(a), 3))
else:
    print("Оберіть пункт від 1 до 10")

# Завдання 4 (2 варіант):
from math import pi, sin, cos, tan
print("""Що хочете зробити?
1.  Додати
2.  Відняти
3.  Помножити
4.  Поділити
5.  Піднести до степені
6.  Знайти квадратний корінь
7.  Знайти кубічний корінь
8.  Знайти sin
9.  Знайти cos
10. Знайти tan""")
m = int(input("Оберіть необхідний варіант з меню: "))
match m:
    case 1:
        a = float(input("Уведіть перше число: "))
        b = float(input("Уведіть друге число: "))
        print("Сума чисел: ", a + b)
    case 2:
        a = float(input("Уведіть перше число: "))
        b = float(input("Уведіть перше число: "))
        print("Різниця чисел: ", a - b)
    case 3:
        a = float(input("Уведіть перше число: "))
        b = float(input("Уведіть перше число: "))
        print("Добуток чисел: ", a * b)
    case 4:
        a = float(input("Уведіть перше число: "))
        b = float(input("Уведіть перше число: "))
        print("Відношення чисел: ", round(a / b), 3)
    case 5:
        a = float(input("Уведіть число: "))
        b = float(input("До якої степені піднести: "))
        print("Відповідь: ", a ** b)
    case 6:
        a = float(input("Уведіть число: "))
        print("Відповідь: ", a ** 0.5)
    case 7:
        a = float(input("Уведіть число: "))
        print("Відповідь: ", a ** (1 / 3))
    case 8:
        a = float(input("Уведіть число: "))
        print("sin(", round(a), ") = ", round(sin(a), 3))
    case 9:
        a = float(input("Уведіть число: "))
        print("cos(", round(a), ") = ", round(cos(a), 3))
    case 10:
        a = float(input("Уведіть число: "))
        print("tan(", round(a), ") = ", round(tan(a), 3))
    case _:
        print("Оберіть пункт від 1 до 10")

# Завдання 5
n = float(input("Уведіть число "))
print("Число парне" if n % 2 == 0 else "Число непарне")

# Завдання 6
day = input("Введіть день тижня: ").lower()
if day == "понеділок" or day == "вівторок" or day == "середа" or day == "четвер"\
        or day == "п'ятниця":
    print("Сьогодні на роботу :(")
elif day == "субота" or day == "неділя":
    print("Сьогодні вихідний :)")
else:
    print("Такого дня не існує")

# Завдання 6 (Варіант 2)
day = input("Введіть день тижня: ").lower()
match day:
    case "понеділок" | "вівторок" | "середа" | "четвер" | "п'ятниця":
        print("Сьогодні на роботу :(")
    case "субота" | "неділя":
        print("Сьогодні вихідний :)")
    case _:
        print("Такого дня не існує")"""
