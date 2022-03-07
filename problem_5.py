
n = 6

for i in range(n):
    print('' * (n-1), end=' ')
    print (' '.join(map(str, str(11 **i))))