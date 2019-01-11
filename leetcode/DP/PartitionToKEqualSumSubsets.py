class Solution:
    def helper(self,k, nums, begin, visited, target, currSum):
        if k < 0 or currSum > target:
            return False
        if currSum == target:
            if k == 1:
                return True
            else:
                return self.helper(k - 1, nums, 0, visited, target, 0)

        for i in range(begin, len(nums)):
            if visited[i]:
                continue
            else:
                visited[i] = True
                if self.helper(k, nums, i + 1, visited, target, currSum + nums[i]):
                    return True
                else:
                    visited[i] = False
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum = 0
        visited = [False for i in range(len(nums))]
        for i in nums:
            sum += i
        if sum % k != 0:
            return False
        else:
            return self.helper(k,nums,0,visited,sum/k,0)


s = Solution()
nums = [4,3,2,3,5,2,1]
k = 4
print(s.canPartitionKSubsets(nums,k))

