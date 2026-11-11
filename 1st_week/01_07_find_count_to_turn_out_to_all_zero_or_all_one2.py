input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    # 1. 0 과 1 을 비교한다.
    # 2. 비교 후, 0은 zero_group 변수에 +1 하거나, 1 이라면 one_group 변수에 +1을 한다.
    # 3. 인덱스 0 과 1 이렇게 순차적으로 값이 변경되는게 있는지 확인하면서, 변하는 곳이 적은 곳으로 하는게 답이다.

    zero_group = 0 # 숫자값이 0 일때
    one_group = 0 # 숫자값이 1 일때

    if string[0] == '0': # 먼저 인덱스 0번째 있는 값을 기준으로 +1 되는 값을 추가한다.
        zero_group +=1
    else:
        one_group +=1

    for i in range(1, len(string)):
        if string[i] != string[i-1]: # string[0] != string[i]
            if string[i] == '0':
                zero_group +=1
            else :
                one_group +=1

    # 이 부분을 채워보세요!
    return min(zero_group, one_group)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)