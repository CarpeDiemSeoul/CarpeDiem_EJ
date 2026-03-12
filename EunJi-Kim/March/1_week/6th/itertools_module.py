from itertools import permutations, combinations, product, combinations_with_replacement
'''
permutations : 순열 / 순서가 중요할 때 - n개 중 r개를 뽑아 일렬로 나열
combinations : 조합 / 순서 상관 없을 때 - n개 중 r개를 순서 상관없이 선택
product : 중복 순열 / 같은 걸 또 뽑아도 될 때 (순서 있음) - 예를 들어 비밀번호 숫자(00, 01, 02...11, 22)를 만들 때
combinations_with_replacement : 중복 조합 / 같은 걸 또 뽑아도 될 때 (순서 없음)
'''

items = ['A', 'B', 'C']

''' 순열 permutations(리스트, 뽑을 개수) '''
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
result = list(permutations(items, 2))

''' 조합 combinations(리스트, 뽑을 개수) '''
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]
result = list(combinations(items, 2))

''' 중복 순열 product(리스트, repeat=뽑을 개수) '''
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ...]
result = list(product(items, repeat=2))

''' combinations_with_replacement(리스트, 뽑을 개수) '''
# 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
result = list(combinations_with_replacement(items, 2))



''' 집합(set) : 중복 제거와 합/교집합 '''
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. 합집합 (전체 모으기)
union_set = set_a | set_b  # {1, 2, 3, 4, 5, 6}

# 2. 교집합 (겹치는 것 찾기)
intersection_set = set_a & set_b  # {3, 4}

# 3. 차집합 (남은 것 확인)
difference_set = set_a - set_b  # {1, 2}

# 4. 원소 추가 및 삭제
set_a.add(10)      # {1, 2, 3, 4, 10}
set_a.discard(2)   # {1, 3, 4, 10} (값이 없어도 에러 안 남)