import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def check_run(visited, now_num):
    # run! 123
    if 0 <= now_num < len(visited) and visited[now_num] >= 3:
        return True
    return False


def check_triplet(visited, now_num):
    # triplet! 111
    cnt = 0
    for i in range(-2, 3):
        if 0 <= now_num + i < len(visited) and visited[now_num + i] >= 1:
            cnt += 1
        else:
            cnt = 0
        
        if cnt == 3:
            return True
        
    return False


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    visited_A = [0] * 10
    visited_B = [0] * 10

    result = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            A = arr[i]
            visited_A[A] += 1
            if check_run(visited_A, A):
                result = 1
                break
            elif check_triplet(visited_A, A):
                result = 1
                break
        else:
            B = arr[i]
            visited_B[B] += 1
            if check_run(visited_B, B):
                result = 2
                break
            elif check_triplet(visited_B, B):
                result = 2
                break

    print(f'#{tc}', result)
