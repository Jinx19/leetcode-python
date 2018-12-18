def binarysearch(numbers, target, start, end):
    l = start
    h = end
    while l + 1 < h:
        mid = (int)((l + h)/2)
        if numbers[mid] == target:
            return mid
        else:
            if numbers[mid] < target:
                l = mid
            else:
                h = mid

    if numbers[l] == target:
        return l

    if numbers[h] == target:
        return h
    return -1


def twosum(numbers, target):
    length = len(numbers)
    for i in range(length):
        remind = target - numbers[i]
        search = binarysearch(numbers,remind,i+1,length-1)
        if search != -1:
            return [i + 1,search + 1]
    return [-1,-1]


def twosumbytwopoints(numbser,target):
    l, h = 0, len(numbser)-1
    sum = numbser[l] + numbser[h]
    while l < h:
        if sum == target:
            return [l+1,h+1]
        if sum < target:
            l += 1
            continue
        if sum > target:
            h -= 1
            continue
    return [-1,-1]


print(twosum([1,4,6,8,9,9],10))

print(twosumbytwopoints([1,4,6,8,9,9],10))