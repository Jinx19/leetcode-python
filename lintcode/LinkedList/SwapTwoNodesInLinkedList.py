from leetcode.LinkedList.ListNode import ListNode

#V1,V2 顺序
def swapNodes(head, v1, v2):
    # write your code here
    if v1 == v2:
        return head
    count = 0
    index1,index2 = count,count
    findv1, findv2 = False, False
    dummp = ListNode(0)
    dummp.next = head
    prev1, prev2 = dummp, dummp,
    while head:
        count += 1
        if not findv1:
            if head.val == v1:
                findv1 = True
                v1Node = head
                index1 = count
            else:
                prev1 = head

        if not findv2:
            if head.val == v2:
                findv2 = True
                v2Node = head
                index2 = count

            else:
                prev2 = head
        head = head.next

    if findv1 and findv2:
        # if v2 is in front of v1, swap them
        if index1 > index2:
            temp = v1Node
            v1Node = v2Node
            v2Node = temp
            temp = prev1
            prev1 = prev2
            prev2 = temp
        if v1Node.next == v2Node or v2Node.next == v1Node:
            prev1.next = v2Node
            v1Node.next = v2Node.next
            v2Node.next = v1Node
        else:
            t = v2Node.next
            prev1.next = v2Node
            v2Node.next = v1Node.next
            prev2.next = v1Node
            v1Node.next = t
    return dummp.next

h = ListNode(10)
h = swapNodes(h, 10, 100)
while h:
    print(h.val)
    h = h.next

