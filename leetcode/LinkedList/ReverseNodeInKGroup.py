from leetcode.LinkedList.ListNode import ListNode


class Solution(object):
    """
    HEAD -->n1-->n2-->n3-->n4-->...-->nk-->nk+1
    ==>
    HEAD -->nk-->nk-1-->nk-2-->...-->n1-->nk+1
    """
    def reverseNextKNodes(self, head, k):
        curt = head
        n1 = curt.next

        # if less k nodes, return null
        for j in range(k):
            curt = curt.next
            if not curt:
                return None

        nk = curt
        nkplus = curt.next

        # reverse

        prev = head
        curt = head.next
        while curt != nkplus:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp

        # last: curt = nk+1,prev = nk,
        # head--> h1
        # nk->nk-1->nk-2->nk-3->....->head
        # nk+1->nk+2->nk+3->...->...
        head.next = nk
        n1.next = nkplus

        return n1

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        while prev:
            prev = self.reverseNextKNodes(prev, k)

        return dummy.next
