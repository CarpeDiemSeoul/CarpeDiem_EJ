import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (N + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue

        for nd, nn in graph[node]:
            new_dist = dist + nd

            if dists[nn] < new_dist:
                continue

            dists[nn] = new_dist
            heappush(pq, (new_dist, nn))
    
    return dists


INF = int(21e8)

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())    # 마지막 연결지점, 도로 개수

    graph = [[] for _ in range(N + 1)]

    for i in range(E):
        s, e, w = map(int, input().split()) # 구간 시작, 끝, 거리

        graph[s].append((w, e))

    result = dijkstra(0)
    print(f'#{tc}', result[N])
