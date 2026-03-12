import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

#1. dfs - stack 없이 재귀함수 방법

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

deltas = [
    [0, 1],     # 동
    [1, 1],     # 동남
    [1, 0],     # 남
    [1, -1],    # 남서
    [0, -1],    # 서
    [-1, -1],   # 서북
    [-1, 0],    # 북
    [-1, 1],    # 북동
]
# 재귀 함수
def dfs(w, h, i, j):
    for k in range(8):
        ni, nj = i + deltas[k][0], j + deltas[k][1]
        
        if 0<=ni<h and 0<=nj<w and not visited[ni][nj]:
            if arr[ni][nj] == 1:
                visited[ni][nj] = True
                dfs(w, h, ni, nj)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    
    # 현재 위치 기준으로 모든 방향을 둘러보면서
    # False로 생성한 visited에 체크
        # False이면 방향 체크하고, True면 체크 안함
    
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(w, h, i, j)
                cnt += 1

    print(cnt)



# 2. dfs - stack 사용 방법
'''
import sys
input = sys.stdin.readline

deltas = [
    [0, 1],     # 동
    [1, 1],     # 동남
    [1, 0],     # 남
    [1, -1],    # 남서
    [0, -1],    # 서
    [-1, -1],   # 서북
    [-1, 0],    # 북
    [-1, 1],    # 북동
]
# 스택배열
def dfs(i, j):
    while stack:
        now_i, now_j = stack.pop()
        for k in range(8):
            ni = now_i + deltas[k][0]
            nj = now_j + deltas[k][1]
            if 0<=ni<h and 0<=nj<w and not visited[ni][nj]:
                if arr[ni][nj] == 1:
                    stack.append([ni, nj])
                    visited[ni][nj] = True


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    
    visited = [[False] * w for _ in range(h)]
    stack= []
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                stack.append([i, j])
                dfs(i, j)
                cnt += 1

    print(cnt)
'''

'''
# bfs - queue 사용 방법

deltas = [
    [0, 1],     # 동
    [1, 1],     # 동남
    [1, 0],     # 남
    [1, -1],    # 남서
    [0, -1],    # 서
    [-1, -1],   # 서북
    [-1, 0],    # 북
    [-1, 1],    # 북동
]

def bfs(i, j, arr, visited):
    queue = [(i, j)]
    visited[i][j] = True

    while queue:
        now_i, now_j = queue.pop(0)
        for k in range(8):
            ni= now_i + deltas[k][0]
            nj= now_j + deltas[k][1]
            if 0 <= ni < h and 0 <= nj < w:
                if not visited[ni][nj] and arr[ni][nj] == 1:
                    queue.append((ni, nj))
                    visited[ni][nj] = True


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j, arr, visited)
                cnt += 1

    print(cnt)
'''

# 같은 구조로 dfs/bfs 차이 보기
'''
deltas = [
    [0, 1],     # 동
    [1, 1],     # 동남
    [1, 0],     # 남
    [1, -1],    # 남서
    [0, -1],    # 서
    [-1, -1],   # 서북
    [-1, 0],    # 북
    [-1, 1],    # 북동
]

def dfs(i, j):
    stack= [(i, j)]
    dfs_visited[i][j] = 1

    while stack:
        now_i, now_j = stack.pop()
        for k in range(8):
            ni = now_i + deltas[k][0]
            nj = now_j + deltas[k][1]
            if 0<=ni<h and 0<=nj<w and not dfs_visited[ni][nj]:
                if arr[ni][nj] == 1:
                    stack.append((ni, nj))
                    dfs_visited[ni][nj] = dfs_visited[now_i][now_j] + 1
                    
                    print("######### dfs #########")
                    pprint(dfs_visited, width=40)
                    print()


def bfs(i, j):
    queue = [(i, j)]
    bfs_visited[i][j] = 1

    while queue:
        now_i, now_j = queue.pop(0)
        for k in range(8):
            ni= now_i + deltas[k][0]
            nj= now_j + deltas[k][1]
            if 0 <= ni < h and 0 <= nj < w:
                if not bfs_visited[ni][nj] and arr[ni][nj] == 1:
                    queue.append((ni, nj))
                    bfs_visited[ni][nj] = bfs_visited[now_i][now_j] + 1

                    print("~~~~~~~~~ bfs ~~~~~~~~~")
                    pprint(bfs_visited, width=40)
                    print()

tc = 0
while 1:
    tc += 1
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    print(f"============== {tc} ==============")
    arr = [list(map(int, input().split())) for _ in range(h)]
    
    dfs_visited = [[0] * w for _ in range(h)]
    bfs_visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not dfs_visited[i][j]:
                dfs(i, j)
                
                print("/////////////////")
                print()

            if arr[i][j] == 1 and not bfs_visited[i][j]:
                bfs(i, j)

                
    # print(cnt)
'''

# dfs/bfs 차이 명확히 보기
'''
deltas = [
    [0, 1],     # 동
    # [1, 1],     # 동남
    [1, 0],     # 남
    # [1, -1],    # 남서
    [0, -1],    # 서
    # [-1, -1],   # 서북
    [-1, 0],    # 북
    # [-1, 1],    # 북동
]

def dfs(i, j):
    stack= [(i, j)]

    cnt = 0
    while stack:
        now_i, now_j = stack.pop()

        for k in range(4):
            ni = now_i + deltas[k][0]
            nj = now_j + deltas[k][1]
            if 0<=ni<h and 0<=nj<w and not dfs_visited[ni][nj]:
                if arr[ni][nj] == 1:
                    stack.append((ni, nj))

        cnt += 1
        dfs_visited[now_i][now_j] = cnt
        
        print("######### dfs #########")
        pprint(dfs_visited, width=40)
        print()
        

def bfs(i, j):
    queue = [(i, j)]
    bfs_visited[i][j] = 1

    while queue:
        now_i, now_j = queue.pop(0)
        for k in range(4):
            ni= now_i + deltas[k][0]
            nj= now_j + deltas[k][1]
            if 0 <= ni < h and 0 <= nj < w:
                if not bfs_visited[ni][nj] and arr[ni][nj] == 1:
                    queue.append((ni, nj))
                    bfs_visited[ni][nj] = bfs_visited[now_i][now_j] + 1

                    print("~~~~~~~~~ bfs ~~~~~~~~~")
                    pprint(bfs_visited, width=40)
                    print()

tc = 0
while 1:
    tc += 1
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    print(f"============== {tc} ==============")
    arr = [list(map(int, input().split())) for _ in range(h)]
    
    dfs_visited = [[0] * w for _ in range(h)]
    bfs_visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not dfs_visited[i][j]:
                dfs(i, j)
                
                print("/////////////////")
                print()

            if arr[i][j] == 1 and not bfs_visited[i][j]:
                bfs(i, j)

                
    # print(cnt)
'''