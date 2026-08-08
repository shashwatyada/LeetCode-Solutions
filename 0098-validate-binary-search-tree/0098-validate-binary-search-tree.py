# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low = float('-inf'), high = float('inf')):
            # An empty tree/node is a valid BST 
            if not node:
                return True

            # current node value must strictly be within (low, high)
            if not(low < node.val < high):
                return False

            # Left child must be < node.val, right child must be > node.val
            return validate(node.left, low, node.val) and validate( node.right, node.val, high)

        return validate(root)