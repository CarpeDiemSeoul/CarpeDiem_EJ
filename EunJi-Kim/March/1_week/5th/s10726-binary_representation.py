import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    light = "OFF"
    
    for i in range(N):
        if (M % 2) & (1 << 0) == 1:
            light = "ON"
        else:
            light = "OFF"
            break
        M //= 2

    print(f"#{tc}", light)       # 마지막 N개의 비트가 모두 켜져 있는지 