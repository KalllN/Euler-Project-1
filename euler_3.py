def prime(n):
  for i in range(2, n):
    if(n%i == 0):
      return False
  return True

N = 600851475143
s = []
for i in range(2, N):
    if prime(i):
      if(N%i == 0):
        s.append(i)
print(s)