# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy head node to attach our results to
        dummy = ListNode(0)
        curr = dummy 
        carry = 0

        # Run as long as there are nodes to process or a carry left over
        while l1 or l2 or carry:
            # Grab values if nodes exists, otherwise treat as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate total sum for this position
            total = val1 + val2 + carry

            # Update carry and find the value for the new node
            carry = total // 10
            digit = total % 10
            
            # Create the new node and link it
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Move l1 and l2 pointers forward safely
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # The true starting point of our result list is right after the dummy node
        return dummy.next