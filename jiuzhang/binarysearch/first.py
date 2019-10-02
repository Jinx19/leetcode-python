class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == "__main__":
    a = 4 if 5 > 3 else 3
    print(a)
