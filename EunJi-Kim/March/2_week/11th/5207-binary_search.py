import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    now = ''

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return 1

        if target < arr[mid]:
            if now == 'L':
                break
            right = mid - 1
            now = 'L'
        elif target > arr[mid]:
            if now == 'R':
                break
            left = mid + 1
            now = 'R'
        
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    # B를 순회하면서 A이진 탐색
    cnt = 0
    for b in B:
        cnt += binary_search(A, b)

    print(f'#{tc}', cnt)
