def get1Num(n):
    num = 0
    count = 0
    while num:
        if num % 2 == 1:
            count += 1
        num = num / 2
    return count
