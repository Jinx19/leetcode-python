class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        ret = []
        if k == 0:
            return ret

        if nums is None or k > len(nums):
            return ret
        i, j = 0, k - 1
        sum = 0
        temp = i
        while temp <= j:
            sum += nums[temp]
            temp += 1
        ret.append(sum)
        while j < len(nums):
            sum -= nums[i]
            i += 1
            j += 1
            if j < len(nums):
                sum += nums[j]
            ret.append(sum)
        return ret
