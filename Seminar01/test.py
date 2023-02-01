import random
n = int(input("Number: "))

list =[]
for i in range(n):
    list.append(random.randint(-50, 50))
print(list)

k = 0
res = 0
temp_res = 0
while k < n:
    if list[k] > 0:
        temp_res += 1
    else:
        if temp_res > res:
            res = temp_res
        temp_res = 0  
    k += 1    
if temp_res > res:
    res = temp_res
print(res)