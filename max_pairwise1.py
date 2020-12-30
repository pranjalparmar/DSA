no = int(input())
lst = []

numbers = input().split()
for i in range(no):
    lst.append(int(numbers[i]))

lst.sort()
a = lst[no-1]
b = lst[no-2]

print(a*b)