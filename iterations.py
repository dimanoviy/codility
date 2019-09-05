print('n = ')
n = int(input())

# for i in range(1, n + 1):
#     print('*' * i)

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    # for j in range(2 * n - 1, 0, -2):
    print('*' * (2 * i - 1))
