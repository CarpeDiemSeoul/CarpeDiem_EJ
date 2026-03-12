nums = [3, 5, 7, 2]
n = len(nums)
target = 10

for bit in range(1 << n):
    current_sum = 0
    selected = []

    for j in range(n):
        if bit & (1 << j):
            current_sum += nums[j]
            selected.append(nums[j])

    if target == current_sum:
        print(f"합이 10인 조합 발견 : {selected}")