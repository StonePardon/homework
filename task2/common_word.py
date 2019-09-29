def common_word(input_text):
    alphabet = input_text.split()
    tmp = {}
    max_num = 0
    ans = ""
    for i in alphabet:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    for keys, values in tmp.items():
        if max_num < values:
            max_num = values
            ans = keys
        elif max_num == values:
            ans = "-"
    del tmp
    return ans
