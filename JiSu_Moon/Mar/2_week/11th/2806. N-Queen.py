# 2806. N-Queen


T = int(input())
  
def Queen(n):
    global ans
  
    if n == N:
        ans += 1
        return
      
    for i in range(N):
        if used[i] == 1:
            continue
        if rup[n+i]==1 or rdown[n-i+N]==1:  # 대각선
            continue
        used[i], rup[n+i], rdown[n-i+N]=1,1,1
        Queen(n+1)
        used[i], rup[n + i], rdown[n - i + N] = 0,0,0
  
  
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    used = [0]*N  # 열 확인
    rup=[0]*(2*N)  # 대각선 확인
    rdown=[0]*(2*N)
  
    Queen(0)
  
    print(f'#{tc} {ans}')