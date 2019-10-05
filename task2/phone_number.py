PHONE_BUTTONS = {
    '0': ' ',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def make_path(input_str, path, ans):
    if input_str == '':
        ans.append(path)
        return
    if input_str[0] != '1':
        for let in PHONE_BUTTONS[input_str[0]]:
            make_path(input_str[1:], path + let, ans)
    else:
        make_path(input_str[1:], path, ans)


def phone_number(number):
    ans = []
    make_path(number, '', ans)
    return ans
