def dfs(N, M, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)

        dfs(N, M, result)

        result.pop()
    
    return

        

N, M = map(int, input().split())

dfs(N, M, [])
