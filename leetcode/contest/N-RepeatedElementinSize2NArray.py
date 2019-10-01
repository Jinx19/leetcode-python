def repeatedNTimes(A):
    """
    :type A: List[int]
    :rtype: int
    """
    A.sort()
    i, j = 0, 1
    while j < len(A):
        if A[i] == A[j]:
            return A[i]
        else:
            i += 1
            j += 1


s = [1, 2, 3, 3]
ret = repeatedNTimes(s)
print(ret)
s = [2, 1, 2, 5, 3, 2]
ret = repeatedNTimes(s)
print(ret)
