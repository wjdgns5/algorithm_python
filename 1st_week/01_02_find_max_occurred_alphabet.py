def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g",
                      "h", "i", "j", "k", "l", "m", "n",
                      "o", "p", "q", "r", "s", "t", "u",
                      "v", "x", "y", "z"]
    max_occurrence = 0 # 최대 횟수
    max_alphabet = alphabet_array[0] # 알파벳 "a"

    for character in alphabet_array:
        char_count = 0 # 알파벳 갯수 셀려고.
        for compare_char in string:
            if compare_char == character:
                char_count += 1

        if char_count > max_occurrence:
            max_occurrence = char_count
            max_alphabet = character

    return max_alphabet

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))