import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################
input = sys.stdin.readline

deltas = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
]

def virus_spreads():
    global max_cnt

    # pop(), append()는 시간을 많이 써서 런타임 생길 가능성이 커져서 배열 크기를 정해놓고 해볼 예정
    # 지문에서 최대 8이라 했으니...
    v_visited = [[False] * M for _ in range(N)]
    queue = [0] * (N * M)
    front = 0
    rear = 0

    for vi, vj in virus:
        queue[rear] = (vi, vj)
        rear += 1
        v_visited[vi][vj] = True
    
    spread_cnt = 0
    while front < rear:
        now_i, now_j = queue[front]
        front += 1
        for k in range(4):
            ni = now_i + deltas[k][0]
            nj = now_j + deltas[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                if nav[ni][nj] == 1:
                    continue

                if nav[ni][nj] == 0 and not v_visited[ni][nj]:
                    queue[rear] = (ni, nj)
                    rear += 1
                    v_visited[ni][nj] = True
                    spread_cnt += 1

                    if (zero_cnt - 3 - spread_cnt) <= max_cnt:
                        return

    max_cnt = max(max_cnt, zero_cnt - 3 - spread_cnt)
    return
    

def build_wall(wall_cnt, start_idx):
    if wall_cnt == 3:
        virus_spreads()
        return

    for k in range(start_idx, N * M):
        r = k // M  # 행 인덱스
        c = k % M   # 열 인덱스
        if nav[r][c] == 0:
            nav[r][c] = 1
            build_wall(wall_cnt + 1, k + 1)
            nav[r][c] = 0
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 0: 빈칸 / 1: 벽 / 2: 바이러스 위치
    nav = [list(map(int, input().split())) for _ in range(N)]

    # 규칙이 보이지 않는다.. 재귀 하면서 완전 탐색 해야겠다..
    # 런타임오류 생길거 같은데...

    # w_visited로 벽을 세운 곳 표시
    # 벽 3개를 다 세웠다면
        # 바이러스 퍼트려보기
        # 남아있는 빈칸이 있는지 확인하기
        # 빈칸 저장해서 최대칸수랑 비교해서 최댓값 저장하기

    # N행을 돌면서 (now_row, N)
        # M열 돌기 (now_col, M)
    virus = []
    max_cnt = -1
    zero_cnt = M * N

    # 바이러스 위치 찾기
    for i in range(N):
        for j in range(M):
            if nav[i][j] == 2:
                virus.append((i, j))
                zero_cnt -= 1
            elif nav[i][j] == 1:
                zero_cnt -= 1

    build_wall(0, 0)

    print(max_cnt)













''' 모듈 사용 방법

import sys
from itertools import combinations

# 빠른 입력을 위해 (백준/SWEA 필수)
input = sys.stdin.readline

def virus_spreads():
    global max_cnt
    
    # BFS용 큐와 방문 배열 초기화
    # N*M이 아주 크지 않다면 매번 만드는 게 안전합니다.
    v_visited = [[False] * M for _ in range(N)]
    queue = [None] * (N * M)
    front = 0
    rear = 0

    # 초기 바이러스 위치 큐에 삽입
    for vi, vj in virus:
        queue[rear] = (vi, vj)
        rear += 1
        v_visited[vi][vj] = True
    
    spread_cnt = 0
    while front < rear:
        now_i, now_j = queue[front]
        front += 1
        
        for di, dj in deltas:
            ni, nj = now_i + di, now_j + dj
            if 0 <= ni < N and 0 <= nj < M:
                # 벽(1)이 아니고 아직 방문 안 했으면 전염
                if nav[ni][nj] == 0 and not v_visited[ni][nj]:
                    v_visited[ni][nj] = True
                    queue[rear] = (ni, nj)
                    rear += 1
                    spread_cnt += 1
                    
                    # [가지치기 추가] 이미 현재 최댓값보다 안전영역이 작아질 것 같으면 중단
                    if zero_cnt - 3 - spread_cnt <= max_cnt:
                        return

    # 안전 영역 계산 및 갱신
    max_cnt = max(max_cnt, zero_cnt - 3 - spread_cnt)

# --- 메인 로직 시작 ---
deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
nav = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty_cells = []
zero_cnt = 0

# 1. 초기 상태 파악 (바이러스 위치, 빈칸 위치, 빈칸 개수)
for i in range(N):
    for j in range(M):
        if nav[i][j] == 2:
            virus.append((i, j))
        elif nav[i][j] == 0:
            empty_cells.append((i, j))
            zero_cnt += 1

max_cnt = 0

# 2. itertools.combinations로 벽 3개 세우는 모든 경우의 수 루프
# combinations(리스트, 개수) -> 리스트에서 3개를 뽑는 조합 생성
for walls in combinations(empty_cells, 3):
    # [벽 세우기]
    for r, c in walls:
        nav[r][c] = 1
        
    # [바이러스 퍼뜨리기]
    virus_spreads()
    
    # [벽 허물기 - 백트래킹]
    for r, c in walls:
        nav[r][c] = 0

print(max_cnt)

'''