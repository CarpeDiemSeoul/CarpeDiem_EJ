"""
1부터 12까지 숫자를 원소로 가진 집합 A

출력: 부분집합의 개수
    조건 1: N개의 원소
    조건 2: 원소의 합이 K
    조건 3: 해당하는 부분집합이 없는 경우 0을 출력
"""

def find_subset(depth, subset, total_sum):
    global cnt
    if total_sum > K:
        return
    
    if depth == 12:
        target_len = len(subset)
        if target_len == N:
            if total_sum == K:
                cnt += 1
        return

    find_subset(depth + 1, subset + [A[depth]], total_sum + A[depth])
    find_subset(depth + 1, subset, total_sum)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    find_subset(0, [], 0)
    print(f"#{tc} {cnt}")