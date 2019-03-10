# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys


def minCoins(coins, m, V):
    if (V == 0):
        return 0

    res = sys.maxsize

    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res


if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    n, m = values[0], values[1]
    coins = [i for i in range(1, n + 1)]
    print(minCoins(coins, n, m))
