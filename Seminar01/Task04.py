# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
chetvert = int(input("Введите номер четверти: "))
if chetvert == 1:
    print("Для", chetvert, "четверти: Х > 0 и Y > 0")
elif chetvert == 2:
    print("Для", chetvert, "четверти: Х < 0 и Y > 0")
elif chetvert == 3:
    print("Для", chetvert, "четверти: Х < 0 и Y < 0")
elif chetvert == 4:
    print("Для", chetvert, "четверти: Х > 0 и Y < 0")