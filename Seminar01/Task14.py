# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
import math
N = int(input("Input number N: "))
for i in range(math.floor(math.log2(N))+1):
    print (2**i)