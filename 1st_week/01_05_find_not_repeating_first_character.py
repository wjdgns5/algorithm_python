# input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!

    alpha_array = [0]* 26

    for i in range (len(string)):
        alpha_array[ord(string[i]) - 97] += 1 #

    for char in string:
        index = ord(char) - 97

        if alpha_array[index] == 1:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))