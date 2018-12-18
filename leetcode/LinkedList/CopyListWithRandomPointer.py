from leetcode.LinkedList.RandomListNode import RandomListNode


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        dummpy = head

        while dummpy:
            copy = RandomListNode(dummpy.label)
            copy.next = dummpy.next
            copy.random = dummpy.random
            dummpy.next = copy
            dummpy = dummpy.next.next

        dummpy = head
        while dummpy:
            if dummpy.next.random:
                dummpy.next.random = (dummpy.random).next
            dummpy = dummpy.next.next

        copyhead = head.next
        
        while head:
            temp = head.next
            head.next = temp.next
            head = temp.next
            if temp.next:
                temp.next = temp.next.next

        return copyhead


H = RandomListNode('a')
H.next = RandomListNode('b')
H.next.next = RandomListNode('c')

H.next.next.next = RandomListNode('d')
H.next.random = H.next.next

s = Solution()
Copy = s.copyRandomList(H)
