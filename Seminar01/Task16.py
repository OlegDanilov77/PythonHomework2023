# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. 

your_list = [int(input('Введите цифру: ')) for i in range(int(input('Введите количество цифр: ')))]
print(your_list)
x = int(input("Введите искомую цифру: "))
result = 0
for a in range(len(your_list)):
    if x == your_list[a]:
        result = result + 1
print(f"Искомая цифра {x} встречается {result} раз")