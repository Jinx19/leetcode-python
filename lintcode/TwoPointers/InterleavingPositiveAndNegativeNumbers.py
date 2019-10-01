class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def interleave(self, A, start, end):
        while start < end:
            temp = A[start]
            A[start] = A[end]
            A[end] = temp
            start += 2
            end -= 2

    def rerange(self, A):
        # write your code here
        left, right = 0, len(A) - 1

        while left <= right:
            while left <= right and A[left] < 0:
                left += 1
            while left <= right and A[right] > 0:
                right -= 1

            if left < right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left += 1
                right -= 1
        # 如果负数个数大于正数个数,第一个负数不需要交叉
        if left > len(A) - left:
            self.interleave(A, 1, len(A) - 1)
        # 如果负数个数小于正数个数,最后一个正数不需要交叉
        elif left < len(A) - left:
            self.interleave(A, 0, len(A) - 2)
        # 负数正数个数相等
        else:
            self.interleave(A, 0, len(A) - 1)


s = Solution()

A = [-13, -8, -12, -15, -14, 35, 7, -1, 11, 27, 10, -7, -12, 28, 18]

s.rerange(A)
print(A)
