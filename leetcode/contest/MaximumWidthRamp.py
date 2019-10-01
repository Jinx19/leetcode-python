from bisect import bisect


def maxWidthRamp(A):
    """
    :type A: List[int]
    :rtype: int
    """
    stack = []
    res = 0
    for i in range(len(A))[::-1]:
        if not stack or A[i] > stack[-1][0]:
            stack.append([A[i], i])
        else:
            j = stack[bisect.bisect_right(stack, [A[i], i])][1]
            res = max(res, j - i)
    return res
