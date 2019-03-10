'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
'''


def removeDuplicates(nums):
    if nums is None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    pre = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if pre == nums[i]:
            continue
        else:
            pre = nums[i]
            count += 1
    return count


nums = [1, 1, 2]
ans = removeDuplicates(nums)
print(ans)
