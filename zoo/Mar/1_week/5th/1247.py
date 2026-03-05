def dfs(curr_x, curr_y, cnt, total_dist):
    global min_dist
    if total_dist >= min_dist:
        return
    if cnt == N:
        final_dist = total_dist + abs(home[0] - curr_x) + abs(home[1] - curr_y)
        if final_dist < min_dist:
            min_dist = final_dist
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dist = abs(curr_x - customers[i][0]) + abs(curr_y - customers[i][1])
            dfs(customers[i][0], customers[i][1], cnt + 1, total_dist + dist)
            visited[i] = 0


t = int(input())

for tc in range(1, t+1):
    N = int(input())

    lst = list(map(int, input().split()))

    cp = (lst[0], lst[1])
    home = (lst[2], lst[3])

    customers = []

    for i in range(4, ((N+2)*2 - 1), 2):
        customers.append((lst[i], lst[i+1]))

    visited = [0] * N
    min_dist = float('inf')

    dfs(cp[0], cp[1], 0, 0)

    print(f"#{tc} {min_dist}")

