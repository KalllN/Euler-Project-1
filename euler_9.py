n = 1000
for a in range(3, n):
    for b in range (a+1, n-1):
        c = (a**2 + b**2)**0.5
        if(a+b+c == 1000):
            print(a*b*c)
            break