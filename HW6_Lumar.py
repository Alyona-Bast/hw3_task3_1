#Завдання 1
my = list(map(float, input("Введіть числову послідовність: ").split()))
print("Найбільший елемент:", max(my))
print("Найменший елемент:", min(my))
print("Сума:", sum(my))
print("Середнє арифметичне:", round(sum(my) / len(my), 3))

#Завдання 2
li1 = list(str(i) for i in input("Введіть перший список: ").split())
li2 = list(str(i) for i in input("Введіть другий список: ").split())
new = list()
for j in li1:
    for k in li2:
        if j == k and j not in new:
            new.append(j)
print(new)
print(new[::-1])
print(sorted(new))
print(sorted(new, reverse=True))

#Завдання 3
a = int(input("З якого числа починати пошук? "))
b = int(input("Яким числом закінчити пошук? "))
ls = []
if a > 2 and a <= b:
    for i in range(a, b + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ls.append(i)
    print(ls)
else:
    print("Проміжок повинен бути в діапазоні [3 ; infinity]")
com = input("Якщо хочете дізнатися їх суму, введіть +\n"
            "Якщо хочете дізнатися їх добуток, введіть *\n")
if com == "+":
    print("Сума:",sum(ls))
elif com == "*":
    n = 1
    for k in ls:
        n *= k
    print("Добуток:", n)
else:
    exit()

#Завдання 4
ls = []
n = int(input("Яка кількість елементів у списку? "))
for i in range(n):
    a = input("Введіть новий елемент")
    ls.append(a)
print(ls)
com = 0
while com != "3":
    com = input("Натисніть 1, якщо хочете вивести список у зворотньому порядку +\n"
                "Натисніть 2, якщо хочете вивести список за зростанням *\n"
                "Натисніть 3 для виходу\n")
    if com == "1":
        print("1:",sorted(ls, reverse=True))
    elif com == "2":
        print("2:", sorted(ls))

#Завдання 5
int_list = list(map(int, input("Введіть послідовність натуральних чисел: ").split()))
for i in int_list:
    if i < 1:
        print("Ви ввели неправильні значення")
else:
    new_list = []
    repeat = int(input("Введіть кількість повторів: "))
    for i in int_list:
        if i % 2 != 0:
            new_list.append(i)
    print(new_list * repeat)
    int_list.clear()

#Завдання 6
new = new_list * repeat
a = int(input("Введіть число: "))
if a in new:
    print("Кількість повторів: ", new.count(a))
    print("Перша позиція у списку: ", new.index(a) + 1)
else:
    print("Такого елемента у списку немає")


