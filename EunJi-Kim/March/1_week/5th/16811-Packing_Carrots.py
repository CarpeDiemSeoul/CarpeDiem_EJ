import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

INIT = 999999

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    C_li = list(map(int, input().split()))      
    C_li.sort()  

    # 대/중/소 구분
    # 같은 크기 당근 상자
    # 빈 상자 안됨
    # 상자에는 N//2를 초과하면 안됨. N이 홀수면 버림
    # 상자별 개수 차이가 최소
    
    max_len = N // 2
    min_diff = INIT
    result = -1

    for i in range(N - 2):  # 소형 범위 | 중/대 에 최소 1개씩은 있어야하니깐 N - 2
        for j in range(i + 1, N - 1):   # 중형 범위

            # 같은 크기 당근은 같은 상자에
            if C_li[i] == C_li[i + 1] or C_li[j] == C_li[j + 1]:
                continue

            box = []
            box.append(C_li[ : i + 1])
            box.append(C_li[i + 1 : j + 1])
            box.append(C_li[j + 1 : N])

            # 각 상자의 크기 계산
            s_len = len(box[0])
            m_len = len(box[1])
            l_len = len(box[2])

            # 조건 확인 (빈 상자 없고, limit 이하)
            if 0 < s_len <= max_len and 0 < m_len <= max_len and 0 < l_len <= max_len:
                diff = max(s_len, m_len, l_len) - min(s_len, m_len, l_len)
                if diff < min_diff:
                    min_diff = diff
                    
    result = min_diff if min_diff != INIT else -1

    print(f"#{tc}", result)   # 최소 차이 출력하기 / 포장할 수 없으면 -1