def dfs(N, M, arr, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        if visited[i]:
            continue

        result.append(arr[i])
        visited[i] = True
        dfs(N, M, arr, result)
        result.pop()
        visited[i] = False
    
    return

        

N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N

dfs(N, M, sorted(arr), [])
