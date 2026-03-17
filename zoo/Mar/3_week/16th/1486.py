"""
높이가 B인 선반이 있음
N명의 점원 각 점원의 키는 H_ij로 나타냄
점원들이 쌓는 탑 = 점원 1명 이상으로
탑의 높이 = 점원 키의 합

탑의 높이가 B 이상인 경우 높이가 가장 낮은 탑

조합 문제
    조건 1) 공집합 안됨
    - 기저 조건: depth = 5


출력: 만들 수 있는 높이가 B이상인 탑중에서 탑의 높이와 B의 차이가 가장 작은 것 출력
"""
def find_min_diff(cnt, lst, total_sum):
    global min_height
    if cnt == N:
        if len(lst) > 0 and total_sum >= B:
            if min_height > total_sum:
                min_height = total_sum
        return
    
    find_min_diff(cnt + 1, lst + [height_line[cnt]], total_sum + height_line[cnt])
    find_min_diff(cnt + 1, lst, total_sum)


T = int(input())

for tc in range(1, T+1):
    # N 점원의 수, B 선반의 높이
    N, B = map(int, input().split())

    # 각 점원의 키를 리스트에 담음
    height_line = list(map(int, input().split()))


    min_height = float('inf')

    find_min_diff(0, [], 0)

    print(f"#{tc} {min_height - B}")