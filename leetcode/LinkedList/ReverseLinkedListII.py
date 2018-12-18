from leetcode.LinkedList.ListNode import ListNode


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p1 = head
        p2 = head.next
        count = 1
        while p1 and p2:
            if count in range(m, n):
                if count == m:
                    p1.next = None
                    l = p1
                t = p2.next
                p2.next = p1
                p1 = p2
                p2 = t
            else:
                pre = p1
                p1 = p1.next
                p2 = p2.next
            count += 1
            if count == n:
                pre.next = p1
                if p2:
                    l.next = p2
                break
        return dummy.next

