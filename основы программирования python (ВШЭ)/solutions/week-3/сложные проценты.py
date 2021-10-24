
P = int(input())
X = int(input())
Y = int(input())
K = int(input())
i = 1
total = X * 100 + Y
dep = int(total * (100 + P) / 100)
if K > i:
    while i != K:
        depT = (dep * (100 + P) / 100)
        dep = depT // 1
        i += 1
    depT = int(depT)
else:
    depT = int(dep)
print(depT // 100, depT % 100)
