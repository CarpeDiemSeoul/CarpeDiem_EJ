T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = arr[0][0]
    Min = 21e8

    di = [0,1]
    dj = [1,0]

    def abc(y, x):
        global cnt, Min

        if y == N-1 and x == N-1:
            if cnt < Min:
                Min = cnt
            return
            
        for d in range(2):
            dy = y+di[d]
            dx = x+dj[d]
            if 0<=dy<N and 0<=dx<N:
                cnt += arr[dy][dx]
                abc(dy, dx)
                cnt -= arr[dy][dx]

    abc(0, 0)
    print(f'#{tc} {Min}')