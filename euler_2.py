s, t, c = 0, 1, 1
N = 4000000
while c < N:
    if c % 2 == 0:
        s += c
    t, c = c, (t + c)
print(s)