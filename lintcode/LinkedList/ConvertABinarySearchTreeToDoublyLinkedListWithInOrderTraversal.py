from collections import deque
from lintcode.LinkedList import DoublyListNode
class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """

    def bstToDoublyList(self, root):
        # write your code here

        dummpy = DoublyListNode(0)

        if root is None:
            return dummpy.next

        ll = root
        stack = deque()
        stack.append(ll)
        while ll.left:
            ll = ll.left
            stack.append(ll)

        pre = dummpy
        while stack:
            treenode = stack.pop()
            doublenode = DoublyListNode(treenode.val)
            doublenode.prev = pre
            pre.next = doublenode
            pre = doublenode
            if treenode.right:
                temp = treenode.right
                stack.append(temp)
                while temp.left:
                    temp = temp.left
                    stack.append(temp)

        return dummpy.next

