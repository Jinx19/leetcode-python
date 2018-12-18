class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        left,right = 0,len(nums) - 1
        count = 0
        length = len(nums)
        left,right =0,len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1
        return count