"""
i번째 수부터 j번째 수까지의 합을 S_ij라고 한다면
S_ij가 M이 되는 경우의 수 출력
그렇다면 S_ij가 M이 되면 그때 cnt += 1을 해줘야겠다
j는 N번째 수까지 가야함
i는 0부터 시작해서 S_ij가 M 보다 큰 동안 i += 1을 증가시켜야함. 
또한 그 직전 A_i를 뺴줘야함
"""
N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

start = 0
s = 0
cnt = 0

for end in range(N):
    s += num_lst[end]

    while s >= M:
        if s == M:
            cnt += 1
        s -= num_lst[start]
        start += 1 

print(cnt)