input_str = "acccdeee"

def summarize_string(input_str):

    char_array = [0] * 26
    result = ""

    # 이 부분을 채워보세요!
    for i in input_str:
        index = ord(i) -97
        char_array[index] += 1

    for i in range(len(char_array)):
        if char_array[i] > 0:
            result += chr(i + 97)+ str(char_array[i])

    return result

print(summarize_string(input_str))