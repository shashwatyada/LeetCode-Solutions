# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case: empty node or found one of the targets
        if not root or root == p or root == q:
            return root

        # recurse on left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right return non-None, current root is LCA
        if left and right:
            return root
            
        # Otherwise, return the non-None child (or None if both are None)
        return left if left else right