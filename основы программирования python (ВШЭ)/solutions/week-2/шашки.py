
s1 = int(input())
s2 = int(input())
f1 = int(input())
f2 = int(input())

k = f2 - s2
i = 0
nextNumbL = s1
nextNumbR = s1

if k < 1:
    print('NO')
else:
    while i != k:
        nextNumbL += 1
        nextNumbR -= 1
        i += 1
        nextNumbL = nextNumbL
        nextNumbR = nextNumbR
    if f1 == nextNumbL or f1 == nextNumbR:
        print('YES')
    else:
        print('NO')
        