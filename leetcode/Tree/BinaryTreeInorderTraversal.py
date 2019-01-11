# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque();
        temp_root = root;
        while temp_root:
            queue.append(temp_root)
            temp_root = temp_root.left

        ret = []
        while queue:
            node = queue.pop()
            ret.append(node.val)
            right = node.right
            while right:
                queue.append(right)
                right = right.left

        return ret


