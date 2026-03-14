"""
1 ~ N 까지 자연수 중에서 중복 없이 M개 선택
단, 고른 수열은 오름차순 = 선택한 수보다 낮은 수는 선택하지 않음.
"""
def recur(cnt, curr_num):
    if cnt == M:
        print(*ans)
        return        
    for nxt_num in range(curr_num, N+1): # 현재 숫자(처음엔 1)에서 N개 까지 수 선택
        ans[cnt] = nxt_num
        recur(cnt + 1, nxt_num + 1) # 선택한 숫자 +1 에서 N개 까지 수 선택

# 기저 조건: M개 선택
# - 시작: 0개 선택
# 다음 재귀 호출: 숫자 N개중 한 개 선택. 단 선택한 수 보다 낮은 수는 보지않음.
N, M = map(int, input().split())

# 정답 배열 설정
ans = [0] * M

recur(0, 1)