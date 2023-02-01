# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random
n = int(input("Number of coins: "))

list =[]
for i in range(n):
    list.append(random.randint(0, 1))
print(list)

num_0 = 0
num_1 = 0

for i in list:
    if i == 0:
        num_0 += 1
    else:
        num_1 += 1
if num_0 < num_1: print(f"Reverse {num_0} coins with 0")
else: print(f"Reverse {num_1} coins with 1")