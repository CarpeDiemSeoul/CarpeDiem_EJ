"""
1 ~ N까지 자연수 중 M 개 선택
단, 같은 수 여러 번 선택 가능 (방문처리 필요 없음)
"""
def recur(cnt):
    if cnt == M:
        print(*ans)
        return

    for num in range(1, N+1): # 1 ~ N까지 수 선택
        ans[cnt] = num
        recur(cnt + 1)

# 기저 조건: M개 선택
# - 시작: 0개 선택
# 재귀 함수 호출: 1~N까지 숫자 중 하나 선택. 단, 선택한 수 다시 선택 가능

N, M = map(int, input().split())

ans = [0] * M

recur(0)