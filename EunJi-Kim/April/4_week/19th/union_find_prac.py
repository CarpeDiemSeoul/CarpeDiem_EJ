
# 1. 부모를 가리키는 집합 만들기
N = 7
parents = [i for i in range(N + 1)]
ranks = [0] * (N + 1)

# 2. 부모 찾는 함수 만들기
def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


# 3. 병합하는 함수 만들기
def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return
    
    # parents[ref_x] = ref_y
    # parents[ref_y] = ref_x

    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_y] < ranks[ref_x]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


union(2, 4)
union(4, 6)

if find_set(2) == find_set(6):
    print("같은 집합")

print(parents, ranks, find_set(4), find_set(5))