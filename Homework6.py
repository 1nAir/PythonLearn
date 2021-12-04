### Exercise 1 ###
text_input = str(input('Введите текст = '))
count = 0
for i in range(len(text_input)):
    if text_input[i] == 'b':
        count += 1
print(count)
### Exercise 2 ###
text_str = str(input('Vvedi = '))
if text_str[0].isupper() and text_str.isalpha():
    for i in range(len(text_str)):
        if text_str[i].isdigit():
            break
    x = 1
    for x in range(len(text_str)):
        z = 1
        if text_str[z].isupper():
            break
        z += 1
    print('Валидация успешно пройдена')
### Exercise 3 ###
text_line = str(input('Введите текст = '))
sum = 0
for i in text_line:
    sum += ord(i)
print('сумма кодов =', sum)
### Exercise 4 ###
import math
x = 2
for i in range(10):
    text = 'pi = {:.' + str(x) + 'f}'
    x += 1
    print(text.format(math.pi))
### Exercise 5 ###
text_string = str(input('Введите текст = '))
text_string_part = text_string.split(' ')
x = 0
xx = ''
for i in range(len(text_string_part)):
    if len(text_string_part[i]) > x:
        x = len(text_string_part[i])
        xx = text_string_part[i]
print(xx)
### Exercise 6 ###
### Exercise 7 ###