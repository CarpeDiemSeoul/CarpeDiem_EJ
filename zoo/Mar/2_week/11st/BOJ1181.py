N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = input()
lst = set(lst)
lst = list(lst)
lst.sort()
lst.sort(key = len)


for i in lst:
    print(i)