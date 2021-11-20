### Exercise 1 ###
first_number = int(input('Первое число = '))
second_number = int(input('Второе число = '))
third_number = int(input('Третее число = '))
fourth_number = int(input('Четвертое число = '))
if first_number >= second_number and first_number >= third_number and first_number >= fourth_number:
    print(first_number)
elif second_number > first_number and second_number >= third_number and second_number >= fourth_number:
    print(second_number)
elif third_number > first_number and third_number > second_number and third_number >= fourth_number:
    print(third_number)
else:
    print(fourth_number)
### Exercise 2 ###
apart_number = int(input('Номер квартиры = '))
if apart_number <= 0:
    print('Введенный номер квартиры равен нулю или меньше нуля')
elif apart_number > 144:
    print('Введенный номер квартиры больше максимального номера квартиры в этом доме')
else:
    entrance_number = ((apart_number - 1) // 36) + 1
    floor_number = (((apart_number - 1) // 4) + 1) - 9 * (entrance_number - 1)
    print('Номер подьезда =', entrance_number, 'Номер этажа =', floor_number)
### Exercise 3 ###
year = int(input('Введите год = '))
divisible_by_400 = year % 400
divisible_by_4 = year % 4
divisible_by_100 = year % 100
if divisible_by_400 == 0:
        print ('Високосный')
elif divisible_by_4 == 0 and divisible_by_100 != 0:
        print ('Високосный')
else:
        print ('Обычный')
### Exercise 4 ###
side_a = float(input('Введите сторону А = '))
side_b = float(input('Введите сторону B = '))
side_c = float(input('Введите сторону C = '))
if (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a:
    print('Треугольник существует')
else:
    print('Треугольник не существует')

