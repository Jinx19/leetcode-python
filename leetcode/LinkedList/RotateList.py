# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head

        temp = head
        stack = deque()

        while temp:
            stack.append(temp)
            last = temp
            temp = temp.next

        k = k % len(stack)
        p = None
        if k == 0:
            return head
        while k > 0:
            p = stack.pop()
            k -= 1

        stack.pop().next = None
        last.next = head
        head = p

        return head
