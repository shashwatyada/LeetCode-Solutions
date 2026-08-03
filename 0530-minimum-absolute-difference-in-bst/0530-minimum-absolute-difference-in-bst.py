# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_def = float('inf')
        self.prev = None

        def inorder(node):
            if not node:
                return 

            # Traversal order: Left -> Root -> Right
            inorder(node.left)

            if self.prev is not None:
                self.min_def = min(self.min_def, node.val - self.prev.val)
            self.prev = node

            inorder(node.right)

        inorder(root)
        return self.min_def