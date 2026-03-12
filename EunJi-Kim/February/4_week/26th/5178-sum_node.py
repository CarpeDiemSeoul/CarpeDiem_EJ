import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드 개수, 리프 노드 개수, 출력한 노드 번호
    arr = [list(map(int, input().split()))for _ in range(M)]   # [노드번호, 자연수]

    # 일단 이진 트리 만들어서 리프 노드 숫자 넣기
    # 현재 노드 번호의 값은
    # 왼쪽 자식 now * 2 + 오른쪽 자식 now * 2 + 1
    # 끝 노드부터 탐색해보자

    now = -1
    tree = [0] * (N + 1)
    for i in range(M):
        tree[arr[i][0]] = arr[i][1]
        if now < arr[i][0]:
            now = arr[i][0] 

    while now > 0:
        if now % 2 != 0:
            tree[now//2] = tree[now - 1] + tree[now]
            now -= 2 
        else:
            tree[now//2] = tree[now]
            now -= 1

    print(f'#{tc}', tree[L])
