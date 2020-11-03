import re

def convert_to_numb(inpt):
    while isinstance(inpt, str) == True:
        if inpt.isdigit() == True:
            return int(inpt)
        elif inpt.lower() == 'pi':
            return int(3.142)
        elif inpt.lower() == 'e':
            return int(2.718)
        else:
            inpt = input('Try enter the Number or Pi or e: ')


def count_type_1(num_1, option, num_2):
    num1 = convert_to_numb(num_1)
    num2 = convert_to_numb(num_2)
    result = 0
    if option == '+' or option == 'plus':
        result = num1 + num2
    elif option == '-' or option == 'minus':
        result = num1 - num2
    elif option == '*' or option == 'multiply':
        result = num1 * num2
    elif option == '/' or option == 'divide':
        if num2 == 0:
            print('Division by 0')
            result = str('Cant count - division by 0')
        else:
            result = num1 / num2
    elif option == '^' or option == 'pow':
        result = num1 ** num2
    return result


def count_type_2(elements):
    number_of_inputs = elements * 2 - 1
    option = ''
    result = 0
    for i in range(number_of_inputs):
        if i == 0:
            result = input('Please, enter number ')
        elif i % 2 == 0:
            local_numb = input('Please, enter number ')
            result = count_type_1(str(result), option, local_numb)
        elif i % 2 == 1:
            option = input('Please, enter option ')
    print('Result for second type of calc is ' + str(result))


def count_type_3(string):
    lst_nub = re.split('[*^/+-]', string)
    lst_opt = re.split('[pi|e1234567890]', string)
    lst_opt_updt = []
    for i in range(len(lst_opt)):
        if lst_opt[i] != '':
            lst_opt_updt.append(lst_opt[i])
            i += 1
    result = lst_nub[0]
    for i in range(len(lst_opt_updt)):
        result = count_type_1(str(result), lst_opt_updt[i], str(lst_nub[i + 1]))
    return result


def count_type_4_eval(string):
    print('Result for fourth type of calculator is ' + str(eval(string)))


if __name__ == '__main__':
    print('First type of calculator')
    a = input('Please, enter first number ')
    op = input('Please, enter option ')
    b = input('Please, enter next one number ')
    print('Result for first type of calculator is ' + str(count_type_1(a, op, b)))

    print('\nSecond type of calculator')
    c = int(input('Please, enter the number of elements '))
    count_type_2(c)

    print('\nThird type of calculator')
    d = input('Please, write text with calcalation ')
    print(str(count_type_3(d)))

    print('\nFourth type of calculator')
    e = input('Please, write text with calcalation ')
    print(str(count_type_4_eval(e)))

