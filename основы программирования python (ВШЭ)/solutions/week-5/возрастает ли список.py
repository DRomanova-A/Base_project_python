
a = input().split()
i = 0
for i in range(len(a)):
    if a[i - 1] < a[i]:
        i += 1
if i == len(a):
    print('YES')
else:
    print('NO')
