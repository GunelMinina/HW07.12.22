# В файле находятся N натуральных чисел через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]
# Найдите это число.


with open('file.txt', 'r') as file:
    some_str = file.readline()

some_list = list(map(int, some_str.split()))
print(some_list)

for i in range(1, len(some_list)):
    if some_list[i] - 1 != some_list[i-1]:
        print(some_list[i]-1)