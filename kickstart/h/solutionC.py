def solve(n,m):
    a, b, c ,d,e = 1, 1, 1,1,1
    for i in range(1, 2*n + 1):
        a = a * i
    # for i in range(1, n + 1):
    #     b = b * i
    # for i in range(1,(n - m) + 1):
    #     c = c * i
    for i in range(1, 2 * (n - m) + 1):
        d = d * i
    for i in range(1, n):
        e = e * i
    res = 1
    temp = n
    for i in range(m):
        res = res * temp
        temp -= 1

    return a - pow(2, m) * (res + e) * d

print(solve(3,2))
#
# file = open("C-small-attempt0.in.txt", "r")
#
# t = int(file.readline())  # read a line with a single integer
# f = open("output.txt", "w")
# for i in range(1, t + 1):
#     line = file.readline().split(' ')
#     n = (int)(line[0])
#     m = (int)(line[1])
#     f.write("Case #{}: {}\n".format(i, solve(n,m)))
#     # check out .format's specification for more formatting options
# f.close()
# file.close()

