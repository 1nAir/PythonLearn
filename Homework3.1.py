### Exercise from chat ###
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x % 2 == 0:
    print('x is odd')
if x % 20 == 0:
    print('x is a multiple of 20')
if x >= 0 and y >= 0:
    print('x and y are both positive')
if (x >= 0 and y >= 0) or (x < 0 and y < 0):
    print('x and y have the ssame sign')
if (x >= 0 and y < 0) or (x < 0 and y >= 0):
    print('x and y have different signs')
if x == y and x == z:
    print('all three names are bound to equal values')
if x != y and x != z and y != z:
    print('all three names are bound to different values')
if (x == y and x != z) or (x == z and x != y) or (z == y and z != x):
    print('two variables store the same value, but the third one is different')
