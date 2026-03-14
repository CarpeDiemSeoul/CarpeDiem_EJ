"""
1~N까지 자연 수 중 M개 선택
단, 같은 수 여러번 가능
단, 고른 수열은 비내림차순.  ex. (2, 1) 이거 안됨
"""
def recur(cnt, curr_num):
    if cnt == M:
        print(*ans)
        return
    
    for nxt_num in range(curr_num, N+1): # 현재 선택한 수부터 N까지 중 선택
        ans[cnt] = nxt_num
        recur(cnt+1, nxt_num)



# 기저 조건: M개 선택
# - 시작: 0개 선택
# 다음 재귀 호출: 본인 포함 ~ N까지 자연수 중 선택


N, M = map(int, input().split())

ans = [0] * M

recur(0, 1)