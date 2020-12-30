def fact_num(n):
    if n <= 1:
        return 1
    else:
        return n*fact_num(n-1)

n = int(input())
print(fact_num(n))