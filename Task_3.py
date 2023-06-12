# Лазарев Олег Евгеньевич, группа 44-22-122, вариант 17

import math
import tkinter as tk

nums = []


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
    except ValueError:
        return 3
    return res


def get_numeric():
    numbers = []

    try:
        str_num = entry.get().split(" ")
        numbers = [float(i) for i in str_num]
        numbers = function(numbers)
    except:
        numbers = "Введено не число"
    if numbers == 1:
        numbers = "Пустой ввод"
    elif numbers == 3:
        numbers = "Число некоректно для подлогарифмического выражения"

    lbl_value["text"] = f"{numbers}"


window = tk.Tk()
window.title("Преобразоатель чисел")
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_entry = tk.Label(master=window, text="Введите числа:")
lbl_entry.grid(row=0, column=0, padx=5)
entry = tk.Entry(master=window, width=25)
entry.grid(row=0, column=1,  padx=10)

btn_enter = tk.Button(master=window, text="Ввести", command=get_numeric)
btn_enter.grid(row=0, column=2, padx=10)

lbl_answer = tk.Label(master=window, text="Ответ:")
lbl_answer.grid(row=1, column=0, padx=10)
lbl_value = tk.Label(master=window, text="")
lbl_value.grid(row=1, column=1, padx=10)

window.mainloop()