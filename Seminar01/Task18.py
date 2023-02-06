# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X.

your_list = [int(input('Введите цифру: ')) for i in range(int(input('Введите количество цифр: ')))]
print(your_list)
x = int(input("Введите проверяемую цифру: "))
result = x - your_list[0]
result_number = your_list[0]
for a in range(len(your_list)):
    if abs(x - your_list[a]) < result:
        result = x - your_list[a]
        result_number = your_list[a]
print(f"Наиболее близкое к {x} число {result_number}")