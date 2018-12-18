# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

from leetcode.Tree.TreeNode import TreeNode


class BSTIterator(object):
    root = None

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root

    def next(self):
        """
        :rtype: int
        """
        q = deque()
        temp = self.root

        # 找到左下角的结点，即最小点
        while temp:
            q.append(temp)
            temp = temp.left

        smallest = q.pop()

        if len(q) > 0:
            parent = q.pop()
            parent.left = smallest.right
        else:
            self.root = smallest.right

        return smallest.val
