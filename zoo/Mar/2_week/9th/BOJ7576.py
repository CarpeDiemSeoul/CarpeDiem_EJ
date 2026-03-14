"""
M 열 size, N 행 size
익은 토마토(1)가 영향을 줄 수 있는 곳(0)은 (왼쪽, 오른쪽, 앞, 뒤)
며칠이 지나면 다 익는가. 그 최소 일수
"""
# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(M, N):
    front = 0
    rear = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                queue[rear] = (y, x)
                rear += 1
                visited[y][x] = 1
    while front < rear:
        curr_y, curr_x = queue[front]
        front += 1

        for d in range(4):
            nxt_y = curr_y + dy[d]
            nxt_x = curr_x + dx[d]
            if 0 <= nxt_y < N and 0 <= nxt_x < M: 
                if visited[nxt_y][nxt_x] == 0 and grid[nxt_y][nxt_x] == 0:
                    visited[nxt_y][nxt_x] = visited[curr_y][curr_x] + 1
                    queue[rear] = (nxt_y, nxt_x)
                    rear += 1

                


M, N = map(int, input().split()) # M 열, N 행

# 토마토 정보 상자(안에 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없는 칸)
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

queue = [0] * (M * N) # queue는 (y, x) 좌표를 담을 건데, 담을수 있는 최대 크기만큼 생성


"""
출력
: 토마토가 모두 익을 때까지의 최소 날짜.
단, 모든 토마토가 익어있는 상태이면 0을 출력
모두 익지 못하는 상황이면 -1
"""
bfs(M, N)
max_days = 0
impossible = False

for y in range(N):
    for x in range(M):
        # 핵심: 원래 토마토가 있었는데(0), 방문하지 못했다면(visited가 0)
        if grid[y][x] == 0 and visited[y][x] == 0:
            impossible = True
            break
        # 전체 기간 중 가장 큰 값 찾기
        if visited[y][x] > max_days:
            max_days = visited[y][x]
    if impossible:
        break

if impossible:
    print(-1)
else:
    # 모든 토마토가 처음부터 익어있었다면 max_days는 1, 결과는 0
    # 빈 상자만 있었다면 max_days는 0, 결과는 -1이 될 수 있으므로 처리 주의
    if max_days == 0: # 혹시 모를 예외 처리
        print(0)
    else:
        print(max_days - 1)