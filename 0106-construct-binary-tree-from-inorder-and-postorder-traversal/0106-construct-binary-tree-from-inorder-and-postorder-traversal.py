# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map each value in inorder to its index for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Start reading postorder from the last element
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            # Base case: no nodes in this subtree range
            if left > right:
                return None
            
            # Pick the current root value for postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            # CRITICAL:  Build right subtree FIRST, then left subtree
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)
            
            return root 

        return helper(0, len(inorder) - 1)