import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def find_max_num_idx(idx):
    if idx >= N:
        return idx
    
    max_idx = idx
    for i in range(idx + 1, N):
        if arr[max_idx] <= arr[i]:   # 최댓값 가진 카드 위치 찾기 / 일의 자리에 가까운 최대수 뽑아오기
            max_idx = i
    
    if max_idx == idx:
        if idx + 1 < N:
            return find_max_num_idx(idx + 1)

    return max_idx

def check(now_idx, now_cnt):
    global max_prize

    if now_cnt == 0:
        max_prize = int(''.join(arr))
        return

    # 1. 최대수 자리 확인
    next_change_idx = find_max_num_idx(now_idx)

    if now_idx >= N - 1 and next_change_idx == now_idx:
        next_change_idx -= 1
    
    arr[now_idx], arr[next_change_idx] = arr[next_change_idx], arr[now_idx]
    check(next_change_idx, now_cnt - 1)
    arr[now_idx], arr[next_change_idx] = arr[now_idx], arr[next_change_idx]


T = int(input())
for tc in range(1, T + 1):
    cards, change_cnt = input().split()
    N = len(cards)
    
    arr = []
    for i in cards:
        arr.append(i)

    max_prize = 0
    check(0, int(change_cnt))

    print(f'#{tc}', ''.join(arr))   # 가장 큰 금액