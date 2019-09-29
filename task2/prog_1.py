def stupid_search(str1):
    i = (str1 + str1).find(str1, 1)
    if i != -1:
        i = len(str1) / i
    else:
        i = 1
    return int(i)


def prefix(input_str):
    m_pref = [0] * len(input_str)
    for i in range(1, len(input_str)):
        k = m_pref[i - 1]
        while k > 0 and input_str[k] != input_str[i]:
            k = m_pref[k - 1]
        if input_str[k] == input_str[i]:
            k = k + 1
        m_pref[i] = k
    return m_pref


def kmp_search(input_str):
    tmp = prefix(input_str)
    pref_len = len(input_str) - tmp[len(tmp) - 1]
    del tmp
    if len(input_str) % pref_len == 0:
        ans = int(len(input_str) / pref_len)
        kmp_str = input_str[0:pref_len]
        kmp_str = kmp_str * ans
        if kmp_str == input_str:
            return ans
    return 1
