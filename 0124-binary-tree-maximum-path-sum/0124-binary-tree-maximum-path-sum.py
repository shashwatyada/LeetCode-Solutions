# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Initialize global max to negative infinity to handle trees with all negative values
        self.max_sum = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0

            # Recursively get maximum path sum from left and right children.
            # Ignore negative sums by comparing with 0.
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))

            # Price of a new path with 'node' as the highest pivot point
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)

            # For recursion back to parent, return the max path going down one side only
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum