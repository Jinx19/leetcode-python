# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from leetcode.Tree.TreeNode import TreeNode


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        stack = deque()
        while curr.left:
            stack.append(curr)
            curr = curr.left

        root = pre = curr

        while stack:
            curr = stack.pop()
            pre.right = curr

            right = curr.right
            while right:
                stack.append(right)
                right = right.left

            pre = curr
            pre.left = None
            pre.right = None

        return root


S = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

print(S.increasingBST(root).__str__())
