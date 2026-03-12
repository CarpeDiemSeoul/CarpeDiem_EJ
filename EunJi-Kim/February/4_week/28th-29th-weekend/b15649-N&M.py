import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def dfs(N, M, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs(N, M, result)

            result.pop()
            visited[i] = False
    
    return

        

N, M = map(int, input().split())

visited = [False] * (N + 1)

dfs(N, M, [])
