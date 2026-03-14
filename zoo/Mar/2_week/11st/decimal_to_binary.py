# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_number = str(remain) + binary_number
        n = n // 2

    return binary_number


print(decimal_to_binary(10))
