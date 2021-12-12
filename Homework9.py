### Exercise 1 ###
def max_number_calc (number_list):
    max_number = max(number_list)
    return max_number
list = [2, 6, 9]
print(max_number_calc(list))
### Exercise 2 ###
def string_and_summ (string, first_number, second_number):
    sum_numbers = first_number + second_number
    string_sum_numbers = string + str(sum_numbers)
    return string_sum_numbers
string = str(input('Введите строку = '))
first_number = int(input('Введите первое число = '))
second_number = int(input('Введите второе число = '))
print(string_and_summ(string,first_number,second_number))
### Exercise 3 ###
def paint (width, height):
    print('*' * width)
    for h in range(height - 2):
        print('*', '*', sep=' ' * (width - 2))
    print('*' * width)
print(paint(4,4))
### Exercise 4 ###
### Exercise 5 ###
def summa (stroka):
    count = 0
    flag = 0
    for i in range(len(stroka)):
        if stroka[i] != ' ' and flag == 0:
            count += 1
            flag = 1
        else:
            if stroka[i] == ' ':
                flag = 0
    return count
text_str = 'dad wrqw tqwtq'
print(summa(text_str))