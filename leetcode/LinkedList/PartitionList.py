class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        from leetcode.LinkedList.ListNode import ListNode
        dummy = ListNode(0)
        dummy.next = head
        greater = ListNode(0)
        headdummy = dummy
        headgreater = greater
        while dummy.next:
            if dummy.next.val < x:
                dummy = dummy.next
            else:
                greater.next = dummy.next
                greater = greater.next
                dummy.next = (dummy.next).next
                greater.next = None
        if headgreater.next:
            dummy.next = headgreater.next
        return headdummy.next
