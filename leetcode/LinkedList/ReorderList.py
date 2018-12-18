"""
L0->L1->L2->L3->L4...->Ln =>
L0->Ln->L1->Ln-1->L2->Ln-2...->
"""
from collections import deque

from leetcode.LinkedList.ListNode import ListNode


def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if head is None or head.next is None or head.next.next is None:
        return head
    #using map
    # h = head
    # count = 0
    # d = {count: head}
    # while h.next:
    #     count += 1
    #     h = h.next
    #     d[count] = h
    #
    # low, high = 0, count
    # while low < high:
    #     d[low].next = d[high]
    #     d[high].next = None
    #     if high + 1 in d:
    #         d[high + 1].next = d[low]
    #     low += 1
    #     high -= 1
    # if low == high:
    #     d[low].next = None
    #     d[low + 1].next = d[low]
    """
    Three steps: 
    1) find mid node and split list to left and right halves 
    2) reverse right part 
    3) merge left and right part
    """
    # slow, fast = head, head.next
    # while fast and fast.next:
    #     slow, fast = slow.next, fast.next.next
    # right, slow.next = slow.next, None
    # p1, p2 = right, right.next
    # p1.next = None
    # while p1 and p2:
    #     t = p2.next
    #     p2.next = p1
    #     p1 = p2
    #     p2 = t
    # while p1:
    #     t = head.next
    #     n = p1.next
    #     head.next = p1
    #     p1.next = t
    #     p1 = n
    #     head = t

    """
    stack
    """
    stack = deque()
    p = head
    while p:
        stack.append(p)
        p = p.next

    count = (len(stack) - 1)/2
    ptr = head
    while count >= 1:
        top = stack.pop()
        tmp = ptr.next
        ptr.next = top
        top.next = tmp
        ptr = tmp
        count -= 1

    stack.pop().next = None


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
# h.next.next.next.next = ListNode(5)
reorderList(h)
while h:
    print(h.val)
    h = h.next
