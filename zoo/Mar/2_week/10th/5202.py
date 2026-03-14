t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]

    time_table.sort(key=lambda x: (x[1], x[0]))

    select_table = []
    curr_end_time = 0

    for i in range(N):
        start_time = time_table[i][0]
        end_time = time_table[i][1]

        if start_time >= curr_end_time:
            select_table.append(time_table[i])

            curr_end_time = end_time

    print(f"#{tc} {len(select_table)}")
