# 1. 1 << n -> 2 ^ n 을 구할 수 있다.
# - 부분 집합의 수를 바로 계산할 수 있다.
arr = [7, 1, 3, 5]

print(f"부분 집합의 수 : {1 << len(arr)}개")

# 2. 전체 부분 집합을 구할 수 있다.
# i = 부분집합 번호
for i in range(1 << len(arr)):
    print(f"{i}번 째 부분집합: ", end=' ')
    subset = []
    # 각 자리수를 모두 확인
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            print(arr[idx], end=' ')

    print()
