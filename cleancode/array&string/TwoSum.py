def twosum(numbers,target):
    map = {}
    for i in range(len(numbers)):
        remind = target - numbers[i]
        if remind in map:
            return [map[remind] + 1,i + 1]
        else:
            map[numbers[i]] = i
    return [-1,-1]

