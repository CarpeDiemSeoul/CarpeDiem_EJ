def dfs(n, lst):
    if n == N:
        print(*lst)
    
    for i in range(1, N+1):
        if visited[i-1] == 0:
            visited[i-1] = 1
            dfs(n+1, lst + [i])
            visited[i-1] = 0


N = int(input())

# 출력 N! 개의 줄에 걸쳐서 모든 수열 출력

"""
dfs(n, lst):

필요한것
종료조건
: 만약 n이 == N과 같아지면
리스트에 담은 것 출력


실행할것?
: i : 1 -> N
"""
visited = [0] * N

dfs(0, [])