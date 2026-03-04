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
    N, hex_num = input().split()

    hex_dic = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7,
               "8" : 8, "9" : 9, "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
    
    # 16진수를 10진수로 변환
    int_N = int(N)
    decimal = 0
    for i in range(int_N):
        now = hex_dic[hex_num[int_N - 1 - i]]
        decimal  += now * (16 ** i)
            
    # 10진수를 2진수로 변환
    binary = ""
    while decimal > 0: 
        binary = str(decimal % 2) + binary
        decimal //= 2

    # 자리수가 맞지 않으면 앞에 0 붙임 / 16진수 한 자리는 2진수 네 자리 => 2**4 = 16
    while len(binary) != (int_N * 4):
        binary = "0" + binary
    
    print(f'#{tc}', binary)
