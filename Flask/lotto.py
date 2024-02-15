import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)

lotto_numbers = generate_lotto_numbers()
print("추출된 로또 번호:", lotto_numbers)

def count_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return len(common_elements)

# 예시 리스트
list1 = [1, 2, 3, 4, 9]
list2 = [4, 5, 6, 7, 8]

common_count = count_common_elements(list1, list2)
print("두 리스트에서 공통된 요소의 개수:", common_count)