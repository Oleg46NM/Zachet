# Лазарев Олег Евгеньевич, группа 44-22-122, вариант 17

import math, unittest

def function(args):
    res = []

    if len(args) == 0:
        return 1
    try:
        for x in args:
            if x <= 0.6:
                y = math.tan(x) ** 2 + math.log(x ** 2, math.e)
            elif x > 0.6:
                y = math.pow(math.e, math.sin(x) ** 2) + math.atan(x)
            res.append(y)
    except TypeError:
        return 2
    except ValueError:  # Число некоректно для подлогарифмического выражения
        return 3
    return res


class Tester(unittest.TestCase):
    def test_notNumber(self):
        self.assertEqual(function(["1"]), 2, "Неправильное считывание не числа")

    def test_isEmpty(self):
        self.assertEqual(function([]), 1, "Неправильное распознание пустого листа")

    def test_impossibleValue(self):
        self.assertEqual(function([0]), 3, "Число некоректно для подлогарифмического выражения")

    def test_getNumbers(self):
        self.assertListEqual(function([2, 3.6, 0.6]), [3.3931904263798787, 2.51616270876759, -0.553608075004024])
        self.assertListEqual(function([-2, -3.6]), [6.160693565161808, 2.805377104526123])


if __name__ == "__main__":
    unittest.main()
