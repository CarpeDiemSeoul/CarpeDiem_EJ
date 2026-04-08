import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

# 섬의 위치 저장해야해고
# 다리 길이는 2 이상
# 시작한 쪽 방향으로만 dfs
# 섬은 다중배열로 저장해서 탐색할 때 섬마다 다리 만들 수 있는지 확인할 수 있도록 [[(i1, j1), (i2, j2)], []]
# visited로 섬 번호 주기 

# 다리를 다 이었는지 체크는 어떻게 할까나...
# 섬끼리 연결되어 있는지 확인을 위한 리스트는 이중 배열로 만들어서 bfs로 연결된 섬들 확인할 수 있도록 [[], [], [], []]

deltas = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
]


def make_bridge(now_i, now_j):
    if now_i < 0 or now_i >= N or now_j < 0 or now_j >= M:
        return



'''
실행부
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 섬 번호 메기기
map = [[0] * M for _ in range(N)]       # 섬 번호 
island_li = []      # 섬 좌표 리스트
island_num = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and map[i][j] == 0:
            queue = [(i, j)]
            front = 0
            rear = 1
            
            island_num += 1
            map[i][j] = island_num
            
            while front < rear:
                now_i, now_j = queue[front]
                front += 1
                for di, dj in deltas:
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 1 and map[ni][nj] == 0:
                            queue.append((ni, nj))
                            rear += 1
                            map[ni][nj] = island_num

            island_li.append(queue)


#2. 다리 만들 수 있는 경우 찾기

bridges = []
for island in island_li:
    for now_i, now_j in island:
        
        for di, dj in deltas:
            ni, nj = now_i + di, now_j + dj

            cnt = 0
            while 0 <= ni < N and 0 <= nj < M:
                if map[now_i][now_j] == map[ni][nj]:
                    break

                if arr[ni][nj] == 1:
                    if cnt >= 2:
                        bridges.append((cnt, map[now_i][now_j], map[ni][nj]))
                    break

                cnt += 1
                ni += di
                nj += dj



# 3. 크루스칼 알고리즘을 위한 준비
# island_num만큼 부모 리스트 생성 (각 섬의 '대장' 저장)
parent = [i for i in range(island_num + 1)]

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False


# 4. 다리 정렬 및 연결
bridges.sort()

total_length = 0
bridge_count = 0

for length, start, end in bridges:
    if union(start, end):
        total_length += length
        bridge_count += 1


# 5. 최종 결과 출력
# 모든 섬이 연결되려면 필요한 다리 수는 (섬의 개수 - 1)개
if island_num > 0 and bridge_count == island_num - 1:
    print(total_length)
else:
    print(-1)

