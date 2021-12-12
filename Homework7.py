### Exercise 1 ###
number_of_day = int(input('Введите номер дня недели = '))
if number_of_day > 7 or number_of_day < 1:
    print('Несуществующий день недели')
else:
    days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
    print(days[number_of_day])
### Exercise 2 ###
cat = {
        'name':str(input('Какое имя у кота?: ')),
        'age':str(input('Сколько прожил кот?: ')),
        'colour':str(input('Какой у кота цвет?: ')),
        'kind':str(input('Какой породы кот?: ')),
      }
print(cat)
### Exercise 3 ###
text_from_keybord = str(input('Введите текст = '))
c = 1
b = -1
x = 0
t = 0
otvet = ''
while x+1 < len(text_from_keybord):
    b += 1
    x += 1
    if  text_from_keybord[b] == text_from_keybord[x]:
        c += 1
    elif text_from_keybord[b] != text_from_keybord[x]:
        t = text_from_keybord[b]
        z=f'-{c} '
        otvet += str(t+z)
        c = 1
z=f'-{c}'
print(otvet + str(text_from_keybord[-1]+z))