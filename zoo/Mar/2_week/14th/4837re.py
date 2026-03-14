A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1 << len(A)):
        subset = []
        for idx in range(len(A)):
            if i & (1 << idx):
                subset.append(A[idx])
        # print(subset)
        if len(subset) == N and sum(subset) == K:
            cnt += 1
    


    print(f"#{tc} {cnt}")
