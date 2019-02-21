haystack = "hello"
needle = "el"


def strStr(haystack: 'str', needle: 'str') -> 'int':
    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_needle == 0:
        return 0

    if len_haystack < len_needle:
        return -1

    for i in range(len_haystack - len_needle + 2):
        for j in range(len_needle):
            if j == len_needle:
                return i
            if i + j == len_haystack:
                return -1
            if haystack[i + j] != needle[j]:
                break


res = strStr(haystack, needle)
print(res)
