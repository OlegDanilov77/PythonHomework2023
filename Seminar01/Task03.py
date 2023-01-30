# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Quarter(xc,yc):
    if xc > 0 and yc > 0:
        return 1
    if xc < 0 and yc > 0:
        return 2
    if xc < 0 and yc < 0:
        return 3
    if xc > 0 and yc < 0:
        return 4
    return 0
    
x = int(input("Введите Х: "))
y = int(input("Введите Y: "))
quarter = Quarter(x,y)
if quarter != 0:
    print("Точка с указанными координатами находится в",Quarter(x,y), "четверти")
else:
    print ("Введены некорректные данные")