from itertools import permutations, combinations, product, combinations_with_replacement

candidates = [(0, 1), (1, 2), (2, 3), (3, 0)]

print("--- 조합 (3개 뽑기) ---")
for wall_triple in combinations(candidates, 3):
    for r, c in wall_triple:
        print(f"({r}, {c})에 벽 설치", end=" / ")
    print()

print("\n--- 순열 (2개 뽑아 나열) ---")
players = ["A", "B", "C"]
for order in permutations(players, 2):
    print(f"공격 순서: {order[0]} -> {order[1]}")



nums = [1, 2, 3, 4, 5, 7]
target = 10

print("합이 10인 조합 찾기 시작!")

current_sum = 0
for combi in combinations(nums, 3):
    if sum(combi) == target:
        print(combi)
        print()



print("합이 10인 조합 요소 개수 상관 없이 찾기")
print(f"목표 합 : {target}")

for i in range(1, len(nums)):
    for combi in combinations(nums, i):
        if sum(combi) == target:
            print(combi)
