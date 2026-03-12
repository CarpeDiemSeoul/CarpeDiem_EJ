def dfs(N, M, now, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(now, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs(N, M, i + 1, result)

            result.pop()
            visited[i] = False
    
    return

        

N, M = map(int, input().split())

visited = [False] * (N + 1)

dfs(N, M, 1, [])
