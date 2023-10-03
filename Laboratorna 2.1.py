import math
def func1():
    a = float(input("Введіть значення α: "))
    b = float(input("Введіть значення β: "))
    z = math.sin(a+b) * math.sin(a-b)
    print(f"z = {z}")
def func2():
    m = float(input("Введіть норму пробігу що спортсмен пробігає за 1-й день [M]: "))
    k = float(input("Введіть процент збільшення норми пробігу [К%]: "))
    distance = 50

    days = 1
    while m < distance:
        m += m * ( k/100)
        days += 1

    print(f"Норма пробігу стане більше 50 км через {days} днів.")

func1()
func2()
