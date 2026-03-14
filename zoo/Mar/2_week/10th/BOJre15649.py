"""
1 ~ N 까지 자연수 중에서 중복 없이 M개 선택
중복 없이 M개. (1, 2) 와 (2, 1)은 다른것
"""
def recur(cnt):
    if cnt == M:
        print(*ans)
        return

    for num in range(1, N+1): # 1 ~ N까지 자연수 중 선택
        if visited[num]: # 선택한 적이 있으면
            continue # 지나간다
        visited[num] = 1
        ans[cnt] = num
        recur(cnt + 1)
        visited[num] = 0
# 기저조건: M
# - 시작: 0개 선택
# 다음 재귀 호출: 숫자 N개 중 하나 선택. (단, 방문 처리 필요)

# N: 1~N 의 수를 선택하는 용도, M 기저조건 용도
N, M = map(int, input().split())

# 방문 처리 필요
visited = [0] * (N + 1) #  [1] ~ [N] 까지 볼거임

# 정답 담을 배열 설정
ans = [0] * M # M개 담을 거임

recur(0)