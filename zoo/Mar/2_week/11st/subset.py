"""
O, X 로 집합에 포함 시킬지 말지 결정.
 -> O or X -> branch: 2

그렇다면 깊이는?
depth 1 : MIN을 데려갈지 말지?
depth 2 : CO을 데려갈지 말지?
depth 3 : TIM을 데려갈지 말지?
"""

arr = ["O", "X"]  # idx 0 -> 1
path = []  # 결과 담을 바구니
name = ["MIN", "CO", "TIM"]


def run(depth):
    if depth == 3:  # 기저 조건 : 세개 다 선택한 경우 담음
        # print(path)
        print_name()
        # OOO, OOX, OXO, OXX, XOO, ...
        return
    for i in range(2):  # idx 0을 선택하거나 1을 선택하거나(두가지)
        path.append(arr[i])  # 바구니에 담음
        run(depth + 1)  # 다음 재귀호출
        path.pop()  # 다 호출되면 마지막꺼 뺌


# 이름 출력 함수
def print_name():
    print("{", end=" ")
    for i in range(3):
        if path[i] == "O":  # path의 i idx가 "O"랑 같다면
            print(name[i], end=" ")  # name의 i idx 값 선택해서 출력
    print("}") # for 다 탈출해야 다 담은 경우


run(0)
