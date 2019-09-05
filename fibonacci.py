print('Enter n number:', end=' ')
n = int(input())
a = 0
print(a)
b = 1
print(b)
i = 1
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1
