input = 20
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    list_value = [2]

    for i in range(2, number, 1):
        is_prime = True

        for j in range(2, i):
            if i% j == 0:
                is_prime = False
                break

        if is_prime:
            list_value.append(i)


    return list_value


result = find_prime_list_under_number(input)
print(result)