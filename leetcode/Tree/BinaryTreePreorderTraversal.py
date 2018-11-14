from collections import deque

from leetcode.Tree.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        q = deque([root])

        while q:
            node = q.pop()
            result.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return result


test = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(test.preorderTraversal(root))
