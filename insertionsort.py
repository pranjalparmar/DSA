n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

def InsertionSort():
    for i in range(1,n):
        temp = a[i]
        j = i-1

        while (j>=0 and a[j]>temp):
            a[j+1] = a[j]
            j-=1

        a[j+1] =  temp

InsertionSort()
print(a)


