"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None

        # Disctionary to map original nodes to their deep copies
        # None maps to none to handle endpoints seamlessly
        old_to_new = {None: None}

        # Create all clone nodes without their pointer connections
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # Connects the next and random pointers for all clones
        curr = head
        while curr:
            clone = old_to_new[curr]
            clone.next = old_to_new[curr.next]
            clone.random = old_to_new[curr.random]
            curr = curr.next

        # Return the clone of the original head node
        return old_to_new[head]