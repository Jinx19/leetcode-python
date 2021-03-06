class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] < k:
                i += 1

            while i <= j and nums[j] >= k:
                j -= 1

            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        return j + 1
