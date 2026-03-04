dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def snail(N):
    y, x, cnt = 0, 0, N**2
    arr[y][x] = cnt
    cnt -= 1
    dr = 0
    while cnt > 0:
        ny = y + dy[dr]
        nx = x + dx[dr]
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 0:
            y, x = ny, nx
            arr[ny][nx] = cnt
            cnt -= 1
        else:
            dr = (dr + 1) % 4
    
    for lst in arr:
        print(*lst)

def find_target(target):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == target:
                print(y+1, x+1)


N = int(input())
target = int(input())

# 출력: 아래 -> 오른쪽 -> 위 -> 왼쪽 순으로 N**2 에서 -1 하면서 채우기 이후 target 위치 찾기
arr = [[0] * N for _ in range(N)]

snail(N)
find_target(target)