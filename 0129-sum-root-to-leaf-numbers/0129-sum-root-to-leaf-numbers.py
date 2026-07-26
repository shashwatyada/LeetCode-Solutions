# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0

            # Append current node digit to path number
            current_sum = current_sum * 10 + node.val

            # If leaf node, return the complete number
            if not node.left and not node.right:
                return current_sum

            # Sum up results from both subtree
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)