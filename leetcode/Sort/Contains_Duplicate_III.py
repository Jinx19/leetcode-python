import collections


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        d = {}
        for i in range(len(nums)):
            m = nums[i]/(t+1)
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < t + 1:
                return True
            if m + 1 in d and abs(nums[i] - d[m+1]) < t + 1:
                return True
            d[m] = nums[i]
            if i >= k:
                d.pop(nums[i-k]/(t+1))
        return False


if __name__ == '__main__':
    s = Solution()
    s.containsNearbyAlmostDuplicate([2, 1], 1, 1)
