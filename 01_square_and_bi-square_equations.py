# 20220606 - Square and Bi-Square Equation Calculator
# !!! WORK IN PROGRESS !!! - it is fine for 'int' numbers ONLY!!!
import math

range_start = -10000
range_end = 10000

print('\nWelcome to Equation Calculator\n')

while True:
    flag = input(f'For Square Equation (ax2 + bx + c = 0) - enter 1,\nFor Bi-Square Equation (ax4 + bx2 + c = 0) - enter 2 : \n')

    if flag == '1':
        print('\nFor (ax2 + bx + c = 0)')
        a = float(input(f'Enter \'a\' = '))
        b = float(input(f'Enter \'b\' = '))
        c = float(input(f'Enter \'c\' = '))
        x = 0

        discriminant = pow(b, 2) - (4 * a * c)
        print(f'\ndiscriminant = {discriminant}\n')

        for i in range(range_start, range_end):
            if ((a * (math.pow(i, 2))) + (b * i) + c) == 0:
                x += 1
                print(f'x{x} = {i}')

        if x == 0:
            print(f'Real value for \'x\' does NOT exist!')

        print(f'\ntested range [{range_start} : {range_end}]')
        break

    elif flag == '2':
        print('\nFor (ay4 + by2 + c = 0)')
        a = float(input(f'Enter \'a\' = '))
        b = float(input(f'Enter \'b\' = '))
        c = float(input(f'Enter \'c\' = '))
        y = 0

        discriminant = pow(b, 2) - (4 * a * c)
        print(f'\ndiscriminant = {discriminant}\n')

        for i in range(range_start, range_end):
            if ((a * (math.pow(i, 4))) + (b * math.pow(i, 2)) + c) == 0:
                y += 1
                print(f'y{y} = {i}')

        if y == 0:
            print(f'Real value for \'y\' does NOT exist!')

        print(f'\ntested range [{range_start} : {range_end}]')

    else:
        print('Enter \'1\' or \'2\'')

    break
