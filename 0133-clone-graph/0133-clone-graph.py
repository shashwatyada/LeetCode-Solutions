"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        # Map to store { original_node : cloned_node}
        cloned = {}

        def dfs (curr):
            # If the node is already cloned, return the cloned instance
            if curr in cloned:
                return cloned[curr]

            # Create a clone of a current node 
            copy = Node(curr.val)
            cloned[curr] = copy

            # Recursively clone all neighbour
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)