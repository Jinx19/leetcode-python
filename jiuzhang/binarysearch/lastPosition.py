class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            return right
        else:
            return -1
