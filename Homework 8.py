### Exercise 1 ###
first_text = str(input('Введите первый текст = '))
second_text = str(input('Введите второй текст = '))
index = 0
uniq_char = ''
for i in range(len(first_text)):
    for y in range(len(second_text)):
        if first_text[i] == second_text[y]:
            if not uniq_char:
                uniq_char += first_text[i]
            check = False
            for c in range(len(uniq_char)):
                if first_text[i] == uniq_char[c]:
                    check = True
            if not check:
                uniq_char += first_text[i]
print(uniq_char)
### Exercise 2 ###
first_set = []
second_set = []
third_set = []
for i in range(1,100,1):
    if i%3==0: first_set.append(i)
    if i%5==0: second_set.append(i)
print('Список кратный трём:', first_set)
print('Список кратный пяти:', second_set)
x1 = set(first_set)
x2 = set(second_set)
m = x1.intersection(x2)
for i in m:  third_set.append(i)
print('Общий список:', third_set)