def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF" # 16진수 표현 (0 ~ 15까지 수)
    hexadecimal_number = "" # 16진수 담을 바구니
    
    if n == 0: # n에 0을 입력하면 0을 리턴하기 위해
        return "0"
    
    while n > 0: # 0보다 클 때까지 16의 나머지를 바구니에 추가(앞으로)
        remain = n % 16
        # remain을 문자열로 변경할 필요 없이 hex_digits의 인덱스로 이용
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        n //= 16
    
    return hexadecimal_number # 다 담았으면 16진수 결과 리턴.

# print(decimal_to_hexadecimal(15))