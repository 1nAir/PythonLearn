### Exercise 1 ###
number = str(input('Введите число = '))
a = int(number[0])
b = int(number[1])
c = int(number[2])
d = int(number[3])
if (a + b) == (c + d):
    print("Счастливый")
else:
    print("Обычный")
### Exercise 2 ###
s = input('Введите число = ')
i = 0
j = len(s) - 1
palindr = True
while i < j:
    if s[i] != s[j]:
        palindr = False
    i += 1
    j -= 1
if palindr:
    print('Палиндром')
else:
    print('Не палиндром')
### Exercise 3 ###
x = float(input("Введите координаты точки х = "))
y = float(input("Введите координаты точки y = "))
radius = 4
formula = (x ** 2 + y ** 2) ** 0.5
if formula > radius:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")
