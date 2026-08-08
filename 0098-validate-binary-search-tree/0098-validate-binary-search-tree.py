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
        stack = []
        curr = root
        prev_val = float('-inf')
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            
            # Value must be strictly greater than the previously visited node
            if curr.val <= prev_val:
                return False
            prev_val = curr.val
            
            curr = curr.right
            
        return True