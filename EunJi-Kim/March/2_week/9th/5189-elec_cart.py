import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def check(current_num, current_sum):
    global min_sum

    if current_sum > min_sum:
        return
    
    if len(stack) == N - 1:
        # 다 돌았으면 사무실로 돌아가기
        current_sum += arr[current_num][0]
        min_sum = min(min_sum, current_sum)
        return
    
    for i in range(1, N):
        if visited[i] == 1:     # 들른 데면
            continue

        visited[i] = 1
        stack.append(i)
        current_sum += arr[current_num][i]
        check(i, current_sum)     
        visited[i] = 0
        stack.pop()
        current_sum -= arr[current_num][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1: 사무실 / 2~N: 관리구역
    # visited로 관리구역 방문 체크
    # 순열이 쓰일거 같음
    # 문제에서는 행이 지금 위치(출발)고, 열이 다음 위치(도착)인거 같음
    # (지금 번호, 다음 번호)

    min_sum = 99999
    visited = [0] * N
    stack = []

    check(0, 0)

    print(f'#{tc}', min_sum)   # 최소 배터리 사용량
    