import sys


def vaild(sourceHash, targetHash):
    for i in range(len(targetHash)):
        if targetHash[i] != 0 and targetHash[i] > sourceHash[i]:
            return False
    return True


def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    lengthS = len(s)
    lengthT = len(t)
    minWindowLength = sys.maxsize
    minStr = ""
    sourceHash, targetHash = [0 for i in range(256)], [0 for i in range(256)]
    for i in range(lengthT):
        targetHash[ord(t[i])] += 1

    j = 0
    for i in range(lengthS):
        while j < lengthS and not vaild(sourceHash, targetHash):
            sourceHash[ord(s[j])] += 1
            j += 1

        if vaild(sourceHash, targetHash):
            if j - i < minWindowLength:
                minWindowLength = j - i
                minStr = s[i:j]
        sourceHash[ord(s[i])] -= 1

    return minStr


if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    n, m = values[0], values[1]
    line = sys.stdin.readline()
    line = line.replace(' ', '')
    t = ''
    for i in range(1, m + 1):
        t += str(i)
    ans = minWindow(line, t)
    print(len(ans))

#
# if __name__ == "__main__":
#     # 读取第一行的n
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split()))
#     n,m =  values[0],values[1]
#     line = sys.stdin.readline()
#     line = line.replace(' ', '')
#     t = ''
#     for i in range(1, m + 1):
#         t += str(i)
#     ans = minWindow(line,t)
#     print(len(ans))
