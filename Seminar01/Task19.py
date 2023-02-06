# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# k = int(input("Введите сдвиг: "))
# num = [1, 2, 3, 4, 5]
# for i in range(k):
#     num.insert(0, num.pop())
# print(num)

# your_list = [int(input('type element: ')) for i in range(int(input('type amount')))]
# k = int(input('type K: ')) % len(your_list)
# print(your_list)
# k_list = your_list[k:] + your_list[:k]

your_list = [int(input('type element: ')) for i in range(int(input('type amount')))]
k = int(input('type K: ')) % len(your_list)
print(your_list)
k_list = your_list[k:] + your_list[:k]
print(k_list)