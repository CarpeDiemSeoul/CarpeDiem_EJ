import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


def check(now_i, now_j, current_sum):
    global min_sum

    current_sum += arr[now_i][now_j]

    if min_sum < current_sum:   # 지금까지의 합이 이미 최소합보다 크면
        return

    if now_i == N - 1 and now_j == N - 1:   # 끝까지 갔다면 최소합 구하기
        min_sum = min(min_sum, current_sum)
        return
    
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = now_i + di, now_j + dj
        if not (0 <= ni < N and 0 <= nj < N):   # 입력 배열 범위를 벗어났다면 다음 단계로
            continue
        check(ni, nj, current_sum)

    return
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 99999

    check(0, 0, 0)

    print(f'#{tc}', min_sum)