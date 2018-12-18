def dfs(length, arrange,result, n, p):
    if length == n:
        # arrange.sort()
        str = ''.join(list(arrange))
        for prrix in p:
            if str.startswith(prrix):
                return
        result.add(str)
        return
    arrange.append('R')
    dfs(length + 1, arrange, result, n, p)
    arrange.pop()
    arrange.append('B')
    dfs(length + 1, arrange, result, n, p)
    arrange.pop()

def permute(n, p):
    # write your code here
    length = 0
    result = set()
    arrange = []
    dfs(length, arrange, result, n, p)
    return len(result)




file = open("A-large.in.txt", "r")

t = int(file.readline())  # read a line with a single integer
f = open("output.txt", "w")
for i in range(1, t + 1):
    line = file.readline().split(' ')
    a = (int)(line[0])
    b = (int)(line[1])
    p = set()
    for j in range(b):
        p.add(file.readline().strip('\n'))
    f.write("Case #{}: {}\n".format(i, permute(a,p)))
    # check out .format's specification for more formatting options
f.close()
file.close()