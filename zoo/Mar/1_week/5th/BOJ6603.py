def dfs(n):

    if len(lst) == 6:
        print(*lst)
        return
    for i in range(n, k):
        lst.append(lotto_nums[i])
        dfs(i + 1)
        lst.pop()


while True:
    lotto_nums_k = list(map(int, input().split()))

    if lotto_nums_k == [0]:
        break

    k = lotto_nums_k[0]
    lotto_nums = lotto_nums_k[1:]  # idx: 0 ~ k-1

    lst = []
    dfs(0)
    print()
