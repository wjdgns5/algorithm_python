def find_max_occurred_alphabet(string):

    character_array = [0]*26 # a ~ z 까지 갯수

    max_index = 0
    max_count = 0

    for compare_char in string:
        if not compare_char.isalpha(): # 문자가 아니라면 통과하라
            continue

        character_array[ord(compare_char) - 97] += 1 # 문자 들어오면 숫자로 변환 후 배열에 +1 값 추가

    for i in range(len(character_array)):
        if character_array[i] > max_count: # 배열 값이 최대인지 비교
            max_index = i # 최대 인덱스 값
            max_count = character_array[i] # 배열 최대 실제 값

    return chr(max_index +97)

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))