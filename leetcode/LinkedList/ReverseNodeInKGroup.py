# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque

from leetcode.LinkedList.ListNode import ListNode


class Solution(object):
    def reverse(self, start, k):
        q = deque()
        pre = start
        while k:
            k -= 1
            q.append(pre)
            pre = pre.next
        head_after_reverse = q.pop()
        curr = head_after_reverse
        while q:
            curr.next = q.pop()
            curr = curr.next
        curr.next = None
        return head_after_reverse, curr

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        pre_right = None
        left, right = head, head
        while right:
            count += 1
            if count == k:
                count = 0
                # save remind node
                remind = right.next

                # get left node and right node after reverse
                new_left, new_right = self.reverse(left, k)

                # first reverse , set return head
                if not pre_right:
                    head = new_left
                else:
                    # connect has revered to curr revered
                    pre_right.next = new_left

                pre_right = new_right
                new_right.next = remind
                left, right = remind, remind
                continue
            right = right.next
        return head


# test


root = ListNode(1)
temp = root
for i in range(2, 6):
    temp.next = ListNode(i)
    temp = temp.next

s = Solution()
head = s.reverseKGroup(root, 3)
