import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

# 2. find-set
def find_set(x):
    if x == group[x]:
        return x
    
    group[x] = find_set(group[x])
    return group[x]

# 3. union
def union(x, y):
    start = find_set(x)
    end = find_set(y)

    if start == end:
        return
    
    group[end] = start


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 인덱스번호(index)가 같이 하고 싶은 번호(value)
    # pair 가 아니고 단독일 수도 있음.

    # 1. make-set
    group = [i for i in range(N + 1)]

    for i in range(M):
        start = arr[i * 2]
        end = arr[i * 2 + 1]
        if find_set(start) != find_set(end):
            union(start, end)

    set_group = set()
    for parent in range(1, N + 1):
        set_group.add(find_set(group[parent]))

    print(f"#{tc}", len(set_group))    # 전체 몇 개의 조