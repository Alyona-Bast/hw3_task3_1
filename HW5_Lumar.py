# 1 завдання
import turtle

name = input("Введіть своє прізвище, ім'я та по батькові ")
if all(x.isspace() or x.isalpha() for x in name) == True and name.istitle() == True:
    print("Дані введено вірно")
else:
    print("Невірно введені дані")

# 2 завдання
a = tuple(map(float, input("Введіть послідовність чисел (не менше 5): ").split()))
if len(a) < 5:
    print("Ви ввели недостатню кількість даних")
else:
    print(a[2] + a[-2] + sum(a)/len(a))

#3 завдання
red = int(input("Введіть інтенсивність червоного кольору: "))
green = int(input("Введіть інтенсивність зеленого кольору: "))
blue = int(input("Введіть інтенсивність синього кольору: "))
if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
    my_tuple = red, green, blue
    print("Колір: ", my_tuple)
else:
    print("Значення інтенсивності кольору має бути в діапазоні [0, 255]")

#4 завдання
from collections import namedtuple
sub = ("алгебра", "геометрія", "історія", "інформатика", "географія")
Marks = namedtuple('Marks', sub)
student1 = Marks(10, 8, 7, 11, 8)
student2 = Marks(11, 5, 9, 8, 6)
student3 = Marks(10, 8, 10, 11, 10)
student4 = Marks(6, 8, 9, 8, 7)
student5 = Marks(10, 7, 9, 9, 10)
print("1. ", student1,"\n2. ", student2, "\n3. ", student3, "\n4. ", student4, "\n5. ", student5)

#5 завдання
a = tuple(map(float, input("Введіть послідовність чисел: ").split()))
print(sorted(a))

#6 завдання
response = input("Залиште свій відгук про курорт \"Морська зірка\": ").lower()
if response.find("меню") != -1 or response.find("спортзал") != -1 or response.find("обслуговування") != -1:
    print("Дякуємо за Ваш відгук")
    if len(response) > 60:
        print("Вам надається знижка 15% на наступне відвідування")
else:
    print("Розкажіть,будь ласка, чи сподобалося Вам наше меню, спортзал та обслуговування")

#6 завдання (2 варіант)
response = input("Залиште свій відгук про курорт \"Морська зірка\": ").lower()
if "меню" in response or "спортзал" in response or "обслуговування" in response:
    print("Дякуємо за Ваш відгук")
    if len(response) > 60:
        print("Вам надається знижка 15% на наступне відвідування")
else:
    print("Розкажіть,будь ласка, чи сподобалося Вам наше меню, спортзал та обслуговування")

#6 завдання (3 варіант)
response = input("Залиште свій відгук про курорт \"Морська зірка\": ").lower()
if response.find("меню") == True or response.find("спортзал") == True or response.find("обслуговування") == True:
    print("Дякуємо за Ваш відгук")
    if len(response) > 60:
        print("Вам надається знижка 15% на наступне відвідування")
else:
    print("Розкажіть,будь ласка, чи сподобалося Вам наше меню, спортзал та обслуговування")




