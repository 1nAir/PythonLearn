### Exercise 1 ###
string = str(input('Строка = '))
integer = int(string)
print(integer)
### Exercise 2 ###
integer = int(input('Целое число = '))
flot = float(integer)
print(flot)
### Exercise 3 ###
flot = float(input('Число с запятой = '))
integer = int(flot)
print(integer)
### Exercise 4 ###
credit_card_number = int(input('Введите номер кредитной карты = '))
string_credit_card_number = str(credit_card_number)
last_numbers = string_credit_card_number[-4:]
print(last_numbers)
### Exercise 5 ###
three_digit_number = int(input('Введите трёхзначное число = '))
string_three_digt_num = str(three_digit_number)
sum_of_digits = int(string_three_digt_num[0]) + int(string_three_digt_num[1]) + int(string_three_digt_num[2])
print(sum_of_digits)
### Exercise 6 ###
first_side = float(input('Первая сторона = '))
second_side = float(input('Вторая сторона = '))
third_side = float(input('Третяя сторона = '))
semi_per = ((first_side + second_side + third_side) / 2)
area_of_triangle = (semi_per * (semi_per - first_side) * (semi_per - second_side) * (semi_per - third_side)) ** 0.5
print(area_of_triangle)
### Exercise 7 ###
sum_number = int(input('Введите число = '))
string_number = str(sum_number)
output = 0
len_string_number = len(string_number)
for i in range(len_string_number):
    output += int(string_number[i])
print(output)
### Exercise 8 ###
determine_number_digits = int(input('Введите число = '))
string_detr_number = str(determine_number_digits)
len_detr_number = len(string_detr_number)
print(len_detr_number)
### Exercise 9 ###
digits_pre_reverse = int(input('Введите число = '))
string_digits_pre_reverse = str(digits_pre_reverse)
digits_reverse = ''
for i in range(len(string_digits_pre_reverse), 0, -1):
    digits_reverse += string_digits_pre_reverse[i-1]
print(digits_reverse)