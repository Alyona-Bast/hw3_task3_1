#Завдання 1
a = 5
b = 10
s = 0
for i in range(a, b + 1):
    s += i
print("Відповідь: ", s)

#Завдання 1 (2 варіант)
a = 5
b = 10
print("Відповідь: ", sum(range(a, b + 1)))

#Завдання 2
f = 1
for i in range(2, int(input("Введіть число ")) + 1):
    f *= i
print("Факторіал цього числа дорівнює: ", f)

#Завдання 2 (2 варіант)
a = int(input("Введіть число "))
f = 1
while a > 1:
    f *= a
    a -= 1
print("Факторіал цього числа дорівнює: ", f)

#Завдання 2 (3 варіант)
import math
print("Факторіал цього числа дорівнює: ", math.factorial(int(input("Введіть число "))))

#Зaвдання 3
n = 1
for i in range (6):
    for j in range (n):
        print("*", end="")
        print(" ", end ="")
    n += 1
    print()

#Зaвдання 4
a = int(input("Введіть перше число "))
b = int(input("Введіть друге число "))
s = 0
for i in range(a, b + 1):
    if i % int((a + b) / 2) == 0:
        s += i
print("Відповідь: ", s)


#Зaвдання 4 (2 варіант)
a = int(input("Введіть перше число "))
b = int(input("Введіть друге число "))
s = 0
for i in range(a, b + 1):
    if i % int(sum(range(a, b + 1)) / len(range(a, b + 1))) == 0:
        s += i
print("Відповідь: ", s)


#Зaвдання 5
a = int(input("Якої висоти прямокутник потрібен? "))
b = int(input("Якої ширини прямокутник потрібен? "))
for i in range (a):
    for j in range (b):
        print("*", end="")
    print()

#Зaвдання 6
x = 3
n = 0
while x:
    x -= 1
    n += 1
    l = input("Введіть логін ")
    p = input("Введіть пароль ")
    if l == "login" and p == "password":
        print("Авторизацію успішно пройдено з", n, "спроби")
        break
    else:
        print("Ви ввели неправельний логін чи пароль")
else:
    print("Кількість спроб вичерпано")






