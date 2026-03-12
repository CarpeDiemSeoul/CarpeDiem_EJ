import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


def merge(left, right):
    global cnt

    result = [0] * (len(left) + len(right))
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    if left[-1] > right[-1]:
        cnt += 1

    return result

def merge_sort(arr):
    N = len(arr)
    if N == 1:
        return arr 

    left = arr[ : N//2]
    right = arr[N//2 : N]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    merge_li = merge(left_li, right_li)
    return merge_li

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0 
    sorted_arr = merge_sort(arr)

    print(f'#{tc}', sorted_arr[N//2], cnt)
