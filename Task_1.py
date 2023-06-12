# Лазарев Олег Евгеньевич, группа 44-22-122, вариант 17

import math, argparse

class UncorrectValue(Exception):
    pass



def function(args):
    res = []
    try:
        for x in args:
            if x <= 0.6:
                y = math.tan(x) ** 2 + math.log(x ** 2, math.e)
            elif x > 0.6:
                y = math.pow(math.e, math.sin(x) ** 2) + math.atan(x)
            res.append(y)
    except:
        raise UncorrectValue
    return res


try:
    parser = argparse.ArgumentParser(description='Преобразователь чисел')
    parser.add_argument('num', type=float, nargs='+', help='Числа для изменения')
    num = parser.parse_args().num
    print(function(num))

except UncorrectValue:
    print("Введены некоректные данные для функции")
except SystemExit:
    print("Введены неверные переменные")
