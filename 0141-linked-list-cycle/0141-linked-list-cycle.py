# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # If the list is empty or has only one node, a cycle can not exist
        if not head or not head.next:
            return False

        slow = head 
        fast = head

        # Traverse the list as long as fast has steps ahead to take
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they crash into each other, a loop is detected
            if slow == fast:
                return True

        # If the fast pointer reaches the end of the list, there is no cycle
        return False