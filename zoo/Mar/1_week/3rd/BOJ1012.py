dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(curr_y, curr_x):
    stack = []
    visited[curr_y][curr_x] = 1
                    
    while True:
        for d in range(4):
            nxt_y = curr_y + dy[d]
            nxt_x = curr_x + dx[d]
            if 0 <= nxt_y < N and 0 <= nxt_x < M:
                if graph[nxt_y][nxt_x] == 1 and visited[nxt_y][nxt_x] == 0:
                    stack.append((curr_y, curr_x))
                    visited[nxt_y][nxt_x] = 1
                    curr_y, curr_x = nxt_y, nxt_x
                    break
        else:
            if stack:
                curr_y, curr_x = stack.pop()
            else:
                break




t = int(input())

for _ in range(t):
    M, N, K = map(int, input().split()) # M: 가로길이, N: 세로길이, K: 배추 좌표

    graph = [[0] * M for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 출력 최소의 배추흰지렁이 마리수
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and visited[y][x] == 0:
                dfs(y, x)
                cnt += 1

    print(cnt)