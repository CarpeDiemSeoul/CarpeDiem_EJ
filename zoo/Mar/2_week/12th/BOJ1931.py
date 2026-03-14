N = int(input())

time_table = [[0] for _ in range(N)]

for n in range(N):
    times = list(map(int, input().split()))
    time_table[n] = times

time_table.sort(key=lambda x: (x[1], x[0]))

select_table = []
end_time = 0

for i in range(N):
    if end_time <= time_table[i][0]:
        select_table.append(time_table[i])
        end_time = time_table[i][1]

print(len(select_table))
