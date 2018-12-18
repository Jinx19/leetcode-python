import sys


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = sys.maxsize
        length = len(nums)
        ret = 0
        nums.sort()
        for i in range(length - 2):
            inner_target = target - nums[i]
            left, right = i + 1, length - 1
            while left<right:
                if abs(target - (nums[i] + nums[left] + nums[right])) < diff:
                    ret =  nums[i] + nums[left] + nums[right]
                    diff = target - ret
                if nums[left] + nums[right] > inner_target:
                    right -= 1
                else:
                    left += 1
        return diff
s = Solution()
nums = [-1,2,1,-4]
target = 1
ret = s.threeSumClosest(nums,target)
print(ret)