import sys


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
# write your code here
        left,right = 0,len(nums) - 1
        diff = sys.maxsize
        nums.sort()
        while left < right:
            diff = min(diff,abs(target - (nums[left] + nums[right])))
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return diff


s =Solution()
nums = [-1, 2, 1, -4]
target = 4
ret = s.twoSumClosest(nums,target)
print(ret)