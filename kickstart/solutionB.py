class dege(object):
    class dege(object):
        def __init__(self, x,start,end):
            self.l = x
            self.start = start
            self.end = end

def specializingvillages(v,graph,path):
    ways = 0

    for k in range(1, v + 1):
        for y in range(1, v + 1):
            for z in range(1, v + 1):
                if graph[y][k] != -1 and grap[k][z] != -1 and grap[y][z] > grap[y][k] + grap[k][z]:
                    grap[y][z] = grap[y][k] + grap[k][z]
                    path[y] = k
                    path[k] = z


    return ways

file = open("A-large-practice.in.txt", "r")

t = int(file.readline())  # read a line with a single integer
f = open("output.txt", "w")
for i in range(1, t + 1):
    a = file.readline().split(' ')
    node = a[0]
    d = a[1]
    row = []
    for x in range(node + 1):
       row.append(-1)
    grap = [row * (node + 1)]
    path = []
    for j in d:
        l = file.readline().split(' ')
        start = l[0]
        end = l[1]
        length = l[2]
        grap[start][row] = length
        path[start] = row

    f.write("Case #{}: {}\n".format(i, specializingvillages(node,grap)))
    # check out .format's specification for more formatting options
f.close()
file.close()


