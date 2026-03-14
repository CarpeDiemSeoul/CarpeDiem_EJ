def backtrack(step, N, s):
    global min_val
    if s >= min_val:
        return

    if step == N - 1:
        final_sum = s + graph[golf[N - 1]][0]
        if final_sum < min_val:
            min_val = final_sum
            return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        golf[step+1] = i
        backtrack(step + 1, N, s + graph[golf[step]][i])
        visited[i] = 0


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1

    golf = [0] * N

    min_val = int(1e9)

    backtrack(0, N, 0)

    print(f"#{tc} {min_val}")
