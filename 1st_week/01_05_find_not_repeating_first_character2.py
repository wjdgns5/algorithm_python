input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    char_list = [0]*26

    for i in range(len(string)):

        value = ord(string[i]) - 97 # 문자를 숫자로 변경 a = 97인데, 97-97 = 0 이 되고 이걸 아래 배열 인덱스로 사용.
        char_list[value] += 1 # char_list[0] = 1 이 될려면 a를 받았을 때 동작하게 되고 나머지 문자를 받았을 때 동작.

    for char in string:
        if char_list[ord(char)-97] == 1:
            return char

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))