class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        wordsdict = dict()
        index = 0
        for i in range(len(nums)):
            if nums[i] in wordsdict:
                continue
            wordsdict[nums[i]] = 1
            nums[index] = nums[i]
            index += 1
        return index


s = Solution()
nums = [1, 3, 1, 4, 4, 2]
ret = s.deduplication(nums)
print(ret)
