import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################



def change(arr, remaining_cnt):
    global max_prize

    state = (''.join(arr), remaining_cnt)
    if state in visited:
        return 
    
    visited.add(state)

    if remaining_cnt == 0:
        max_prize = max(max_prize, int(''.join(arr)))
        return

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            change(arr, remaining_cnt - 1)
            arr[j], arr[i] = arr[i], arr[j]

    return

T = int(input())
for tc in range(1, T + 1):
    cards, change_cnt = input().split()
    cards = list(cards)

    max_prize = 0
    visited = set()
    change(cards, int(change_cnt))

    print(f'#{tc}', max_prize)   # 가장 큰 금액



"""

def swap(rep):
    if rep == 0:
        global max_prize
        local_prize = int(''.join(cards))
        max_prize = max(max_prize, local_prize)
        return
    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            # i와 j를 교환
            cards[i], cards[j] = cards[j], cards[i]

            # 교환한 결과의 상금 조합이 이번 회차에서 만든적 있는지
            local_prize = int(''.join(cards))
            # 이미 만들지 못한 숫자의 경우
            if local_prize not in memo[n - rep]:
                # 만약 처음 만든 경우 해당 집합에 추가하고
                memo[n - rep].add(local_prize)
                # 다음 교환을 실행하러 간다
                swap(rep - 1)

            # 이 길의 끝을 보았다면 원복시킨다
            cards[i], cards[j] = cards[j], cards[i]



tests = int(input())
for test_case in range(1, tests + 1):
    cards, n = input().split()
    cards = list(cards)
    n = int(n)

    # 내가 특정 회차에 어떤 조합을 만든적 있는지
    memo = [set() for _ in range(n)]
    # memo[0] == 한번 교환했을 때 만들 수 있었던 조합을 담는 집합
    # memo[1] == 두번 교환했을 때 만들 수 있었던 조합을 담는 집합
    # ...

    max_prize = 0
    swap(n)

    print(f'#{test_case} {max_prize}')

"""