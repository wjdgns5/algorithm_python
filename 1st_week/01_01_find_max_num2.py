def find_max_num(array):

    for number in array:
        is_max_num = True
# number : 최종 비교값 결과물
# compare_number : 중간 비교값
        for compare_number in array:
            if number < compare_number:
                is_max_num = False

        if is_max_num: # TRUE 인 NUMBER 값 찾아서 주면 된다.
            return number

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))