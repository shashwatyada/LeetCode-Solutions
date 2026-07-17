# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        # dummy node handles cases where 'left' is the very first node safely 
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy 

        # Step 1: March 'prev' until it is right before the reversal zone
        for _ in range(left - 1):
            prev = prev.next

        # Curr is the first Node iniside our reversal zone 
        curr = prev.next 

        # Step 2: Perform the link rolling steps right - left times
        for _ in range(right - left):
             # Target the Node to be pulled forward
            nxt = curr.next 

            # Sever nxt from its current spot and hook curr to what follows 
            curr.next = nxt.next

            # Splice nxt right between prev and prev.next
            nxt.next = prev.next 
            prev.next = nxt

        # The true head is safely preserved right behind our dummy anchor
        return dummy.next