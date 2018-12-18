class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def quicksort(self,nums,k,start,end):
        piv = nums[start]
        left,right = start,end
        while left < right:
            while left < right and nums[left] < piv:
                left += 1
            while left < right and nums[right] > piv:
                right -= 1
            if left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1

        if nums[right] < nums[start]:
            nums[start] = nums[right]
            nums[right] = piv

        if right - start + 1 > k:
            return self.quicksort(nums,k,start,right - 1)
        elif right - start + 1 < k:
            return self.quicksort(nums,k - right + start - 1,right + 1,end)
        else:
            return nums[right]

    def kthSmallest(self, k, nums):
        # write your code here
        return self.quicksort(nums,k,0,len(nums) - 1)

solution = Solution()
k = 10
nums = [1,2,3,4,5,6,8,9,10,7]
ans = solution.kthSmallest(k,nums)
print(ans)