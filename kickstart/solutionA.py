#round f 2018
def anagrams(a, b):
    # letters = list(0 for i in range(26))
    #     letters = {c: 0 for c in 'ABCDEFGHIJKMNOPQRSTUVWXYZ'}
    # for i in a:
    #     letters[i] += 1

    for j in range(len(b) - len(a) + 1):
        subb = b[j: j+len(a)]
        list_str1 = list(a)
        list_str1.sort()
        list_str2 = list(subb)
        list_str2.sort()
        if list_str1 == list_str2:
            return True
    return False


def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i, length)]


def commonanagrams(a, b):
    count = 0
    all_substrings = get_all_substrings(a)

    for substring in all_substrings:
        if anagrams(substring, b):
            count += 1
    return count


# print(commonanagrams("ABB", "BAB"))
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
file = open("A-large-practice.in.txt", "r")

t = int(file.readline())  # read a line with a single integer
f = open("output.txt", "w")
for i in range(1, t + 1):
    length = int(file.readline())
    a = list(file.readline())
    astr = a[:length]
    b = list(file.readline())
    bstr = b[:length]
    count = commonanagrams(astr, bstr)
    f.write("Case #{}: {}\n".format(i, count))
    # check out .format's specification for more formatting options
f.close()
file.close()



