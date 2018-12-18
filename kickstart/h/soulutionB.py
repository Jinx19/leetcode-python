def solve(nums, N):
    res = 0
    if N % 2 == 0:
        len = (int)(N / 2)
    else:
        len = (int)((N + 1) / 2)

    for i in range(N):
        temsum = 0
        for j in range(i, i + len):
            if j < N:
                temsum += (int)(nums[j])
        res = max(res,temsum)
    return res

file = open("B-small-attempt0.in.txt", "r")

t = int(file.readline())  # read a line with a single integer
f = open("output.txt", "w")
for i in range(1, t + 1):
    N = int(file.readline())
    nums = list((file.readline().split("\n")[0]))
    f.write("Case #{}: {}\n".format(i, solve(nums, N)))
    # check out .format's specification for more formatting options
f.close()
file.close()