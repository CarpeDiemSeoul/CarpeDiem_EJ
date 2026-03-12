def dfs(N, M, now, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(now, N + 1):
        result.append(i)
        if result[-1] <= i:
            dfs(N, M, i, result)
        else:
            dfs(N, M, i + 1, result)

        result.pop()
    
    return

        

N, M = map(int, input().split())

dfs(N, M, 1, [])
