def binary_to_decimal(binary_str):
    decimal_number = 0  # 10진수 담을 바구니
    pow = 0  # 2의 지수는 0부터 시작하기 위해

    # binary_str을 리버스 시켜줘야 2^0 부터 2^1, 2^2, ... 더할 수 있음
    for digit in reversed(binary_str):
        if digit == "1":  # 2진수의 각 자리가 1일 때만 2^pow를 더해줘야함
            decimal_number += 2**pow
        pow += 1  # 자리를 바꿀 때 마다 pow + 1 시켜줘야함

    return decimal_number  # 2진수를 10진수로 다 변환했으면 결과 리턴


print(binary_to_decimal("11101"))
