class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def quickSort(self, start, end, nums, k):

        i, j = start, end
        v = nums[start]

        while i <= j:
            while i <= j and nums[i] < v:
                i += 1
            while i <= j and v < nums[j]:
                j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        if start + k - 1 <= j:
            return self.quickSort(start, j, nums, k)
        if start + k - 1 >= i:
            return self.quickSort(i, end, nums, k - (i - start))
        return nums[j + 1]

    def median(self, nums):
        size = len(nums)
        if size % 2 == 0:
            k = size / 2
        else:
            k = (size + 1) / 2
        return self.quickSort(0, size - 1, nums, k)


s = Solution()
print(s.median([7, 9, 4, 5]))