class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1
        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] < mid:
                left = mid + 1
            elif A[mid] > mid:
                right = mid - 1
            else:
                res = mid
                right = mid - 1
        return res