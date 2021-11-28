### Exercise 1 ###
for i in range(100):
    z = (i + 1) % 7
    if z == 0:
        print(i + 1)
### Exercise 2 ###
number = int(input('Введите число = '))
x = number
z = 1
for i in range(number):
    z *= x
    x = x - 1
print(z)
### Exercise 3 ###
character = int(input('Введите число = '))
for i in range(character):
    print(i + 1,'* 5 =', (i + 1) * 5)
### Exercise 4 ###
height = int(input('Введите высоту = '))
width = int(input('Введите ширину = '))
x = ' '
print('*' * width)
for h in range(height - 2):
    print('*', '*', sep=x * (width - 2))
print('*' * width)
### Exercise 5 ###
alist = [0,5,2,4,7,1,3,19]
x = 0
for i in range(len(alist)):
    z = alist[i] % 2
    if z != 0:
        x += 1
print(x)
### Exercise 6 ###
x = [int(i) for i in input('Введите число = ').split()]
b = x
for i in range(len(x)):
    c = int(x[i]) * 2
    b += [c]
print(b)
### Exercise 7 ###
x = [int(i) for i in input('Введите число = ').split()]
print(x)
c = 0
element_range = len(x)
for i in range(element_range):
    c += x[i]
print(c / element_range)
### Exercise 8 ###
x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
summa = 0
for i in range(len(x)):
    print(x[i])
    for z in range(len(x[i])):
        summa += x[i][z]
print(summa)

