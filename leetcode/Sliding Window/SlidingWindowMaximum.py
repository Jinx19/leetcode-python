from collections import deque


def inQueue(queue, num):
    while len(queue) != 0 and queue[-1] < num:
        queue.pop()

    queue.append(num)


def outQueue(queue, num):
    if queue[0] == num:
        queue.popleft()


def maxSlidingWindow(nums, k):
    ans = []
    queue = deque()

    if nums is None or len(nums) == 0:
        return ans

    for i in range(k - 1):
        inQueue(queue, nums[i])

    for i in range(k - 1, len(nums)):
        inQueue(queue, nums[i])
        ans.append(queue[0])
        outQueue(queue, nums[i - k + 1])
    return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
ans = maxSlidingWindow(nums, k)
print(ans)
