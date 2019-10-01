class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        length = len(nums)
        if length < 3:
            return triplets

        nums.sort()

        for i in range(length):
            target = 0 - nums[i]

            hashmap = {}
            for j in range(i + 1, length):
                item_j = nums[j]
                if (target - item_j) in hashmap:
                    triplet = [nums[i], target - item_j, item_j]
                    if triplet not in triplets:
                        triplets.append(triplet)
                else:
                    hashmap[item_j] = j
        return triplets

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        reslist = []
        for i in range(len(res)):
            reslist.append(list(res.pop()))
        return reslist


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
triplets = s.threeSum2(nums)
print(triplets)
