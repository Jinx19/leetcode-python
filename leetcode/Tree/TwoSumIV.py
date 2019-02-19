# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

from leetcode.Tree.TreeNode import TreeNode


class Solution:
    def search(self, root, k,node):
        if root is None:
            return False
        if root is not node and root.val == k:
            return True
        if root.val < k:
            return self.search(root.right, k)
        if root.val > k:
            return self.search(root.left, k)

    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        queue = deque()
        queue.append(root)
        tag = False
        while len(queue) > 0 and tag is False:
            node = queue.popleft()
            key = k - node.val
            tag = self.search(root, key,node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return tag

s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)


result = s.findTarget(root,4)
if result:
    print("True")
else:
    print("False")
