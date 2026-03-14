t = int(input())

for _ in range(t):
    lst = list(map(int, input().split()))

    tc = lst[0]
    line = lst[1:]

    cnt = 0

    for i in range(1, 20):
        for j in range(i):
            if line[i] < line[j]:
                cnt += 1
    
    print(tc, cnt)