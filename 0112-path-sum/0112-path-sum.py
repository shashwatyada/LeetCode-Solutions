# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # If node is empty, no path exist 
        if not root:
            return False

        # Check if we are at a leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        # Subtract current node value and check left and right subtree
        remaining_val = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_val) or
                self.hasPathSum(root.right, remaining_val))