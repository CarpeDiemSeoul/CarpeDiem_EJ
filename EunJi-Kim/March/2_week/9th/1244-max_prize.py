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
    cards, change_cnt = input().split()
    N = len(cards)
    cards = list(cards)

    
    

    print(f'#{tc}', cards)   # 가장 큰 금액