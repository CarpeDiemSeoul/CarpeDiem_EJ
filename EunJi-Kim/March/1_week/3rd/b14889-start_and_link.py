import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def dfs(idx, count):
    global min_diff

    
    for i in range(idx, N):
        for j in range(i + 1, N):
            if not checked[j]:
                checked[j] = True
                dfs(j, count)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 뽑았는지 체크는 check 배열로 True/False 하고
# team1, team2

checked = [False] * N
min_diff = float('inf')

start_team = []
link_team = []

dfs(0, 0)






