class Solution(object):
    def findKth(self,nums1,nums2,k):
        if len(nums1) == 0:
            return nums2[0]
        if len(nums2) == 0:
            return nums1[0]
        if k == 1:
            return min(nums1[0],nums2[0])
        mid = (int)(k/2)
        a = nums1[mid - 1] if len(nums1) >= mid else None
        b = nums2[mid - 1] if len(nums2) >= mid else None

        if b is None or (a is not None and a < b):
            return self.findKth(nums1[mid:],nums2,k - mid)
        return self.findKth(nums1,nums2[mid:1],k-mid)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            left = self.findKth(nums1,nums2,n/2)
            right = self.findKth(nums1,nums2,n/2 + 1)
            return (left + right)/2
        else:
            return self.findKth(nums1,nums2,(n + 1)/2)


s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1,nums2))