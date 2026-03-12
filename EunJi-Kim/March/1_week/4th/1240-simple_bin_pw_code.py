import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

code_dic = {
    "0001101" : 0,
    "0011001" : 1, 
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9,
}

def find_start_idx(N, M):
    # 뒤에서부터 1을 찾음
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == "1":
                return i, j
            
    return 0
                

def is_find_code(N, M):
    i, j = find_start_idx(N, M)

    odd = 0 
    even = 0

    for k in range(8):
        num = ''
        for l in range(7):
            num = arr[i][(j - l) - (7 * k)] + num 
        
        if k % 2 == 0:  # 실행문에서 가로를 뒤에서부터 탐색하기 때문에 인덱스 짝수는 똑같이 짝수
            even += code_dic[num]
        else:
            odd += code_dic[num]

    if (odd * 3 + even) % 10 == 0:
        return odd + even

    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = is_find_code(N, M)
    
    print(f'#{tc}', result)