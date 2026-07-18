# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node protects against having to wipe out the initial head node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                duplicate_val = prev.next.val
                while prev.next and prev.next.val == duplicate_val:
                    prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next