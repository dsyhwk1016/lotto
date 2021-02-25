from random import randint


# 겹치지 않는 num개의 랜덤 정수 생성
def generate_numbers(num):
    numbers = []
    while len(numbers) < num:
        temp = randint(1, 45)
        if temp not in numbers:
            numbers.append(temp)
    return numbers


# 당첨 번호 7자리 생성
def draw_winning_numbers():
    winning_number = generate_numbers(7)
    return sorted(winning_number[:6]) + winning_number[6:]


# 당첨번호와 비교해 맞은 개수 반환
def count_matching_numbers(list1, list2):
    count = 0
    for i in list1:
        if i in list2:
            count += 1
    return count


# 맞은 개수에 따른 당첨금 반환
def check(numbers, winning_number):
    normal = count_matching_numbers(numbers, winning_number[:6])
    bonus = count_matching_numbers(winning_number[6:], numbers)
    if normal == 6:
        return 1000000000
    elif normal == 5 and bonus == 1:
        return 50000000
    elif normal == 5:
        return 1000000
    elif normal == 4:
        return 50000
    elif normal == 3:
        return 5000
