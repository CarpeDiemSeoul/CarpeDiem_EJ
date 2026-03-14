def change(cnt, charge, charge_cnt):
    global min_charge_cnt

    if charge_cnt >= min_charge_cnt:
        return

    if cnt == N:
        min_charge_cnt = charge_cnt
        return

    change(cnt + 1, bus_stop[cnt] - 1, charge_cnt + 1)

    if charge > 0:
        change(cnt + 1, charge - 1, charge_cnt)


t = int(input())

for tc in range(1, t + 1):
    bus_stop = list(map(int, input().split()))

    N = bus_stop[0]

    min_charge_cnt = 51

    change(2, bus_stop[1] - 1, 0)

    print(f"#{tc} {min_charge_cnt}")
