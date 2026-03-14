"""
시작 지점 -> 가능한 모든 경로 -> 시작 지점으로 돌아오기
"""
def recur(cnt, curr_nod, total_sum):
    global min_val
    if total_sum >= min_val:
        return
    if cnt == N-1:
        final_sum = total_sum + graph[curr_nod][0]
        if min_val > final_sum:
            min_val = final_sum
            return
    for nxt_nod in range(1, N): # 열 [1] ~ [N-1] 중 선택
        if visited[nxt_nod]:
            continue
        visited[nxt_nod] = 1
        recur(cnt+1, nxt_nod, total_sum + graph[curr_nod][nxt_nod])
        visited[nxt_nod] = 0

# 기저조건: 가능한 모든 경로 다 탐색 후
# - 시작: [0]에서 시작해서 마지막 경로까지
# 다음 재귀 함수: 깊이 + 1, 노드위치, 현재까지 합 갱신
t = int(input())

for tc in range(1, t+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    min_val = int(1e9)

    recur(0, 0, 0)

    print(f"#{tc} {min_val}")    