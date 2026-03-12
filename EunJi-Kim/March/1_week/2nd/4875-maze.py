'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''


###############################


deltas = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0],
]    

def bfs(start):
    si, sj = start[0], start[1]
    queue = [(si, sj)]
    visited[si][sj] = 1

    while queue:
        si, sj = queue.pop(0)
        for k in range(4):
            ni, nj = si + deltas[k][0], sj + deltas[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[ni][nj] == '0':
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[si][sj] + 1
                elif visited[ni][nj] == 0 and arr[ni][nj] == '3':
                    return 1
                
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    start = [0, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = [i, j]

    visited = [[0] * N for _ in range(N)]

    print(f'#{tc}', bfs(start))
