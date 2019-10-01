# 15. 全排列
# 给定一个数字列表，返回其所有可能的排列。
#
# 样例
# 给出一个列表[1,2,3]，其全排列为：
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# 挑战
# 使用递归和非递归分别解决。


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def dfs(self, length, arrange, nums, result, n):
        if length == n:
            result.append(list(arrange))
            return
        for i in range(len(nums)):
            arrange.append(nums[i])
            self.dfs(length + 1, arrange, nums[0:i] + nums[i + 1:], result, n)
            arrange.pop()

    def permute(self, nums):
        # write your code here
        length = 0
        result = []
        arrange = []
        n = len(nums)
        self.dfs(length, arrange, nums, result, n)
        return result
