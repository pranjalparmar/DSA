def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

a, b = [int(i) for i in input().split()]
lcm = a*b/GCD(a,b)

print(int(lcm))