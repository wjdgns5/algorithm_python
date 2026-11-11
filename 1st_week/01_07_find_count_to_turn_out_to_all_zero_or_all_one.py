input = "011110111101111"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    zero_group = 0 # 0 일때
    one_group = 0 # 1 일때

    if string[0] == '0':
        zero_group += 1
    else:
        one_group += 1

    for i in range(1, len(string), 1): # 인덱스 1부터 시작
        if string[i] != string[i - 1]: # 인덱스 0 과 1 비교 후 값이 다른지 확인.
            if string[i] == '0': # 만약, 다른 값이 0 이라면
                zero_group += 1 # zero_grop 값을 +1 증가
            else: # 만약, 값이 1 이라면
                one_group += 1 # one_group 값을 +1 증가
    return min(zero_group, one_group) # 그리고 마지막, zero_group 과 one_group 값 두개 중 최소값을 출력 


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)