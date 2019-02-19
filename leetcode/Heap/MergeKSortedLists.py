# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from leetcode.LinkedList.ListNode import ListNode

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        heap = PriorityQueue()

        for i in range(len(lists)):
            heap.put(lists[i])
        head = ListNode(0)
        tail = head
        while heap is None:
            smallest = heap.get()
            tail.next = ListNode(smallest.val)
            tail = tail.next
            if smallest.next is not None:
                heap.put(smallest.next)
        return head.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1,list2,list3]
so = Solution()
res = so.mergeKLists(lists)
while res is not None:
    print(res.val)
    res = res.next


