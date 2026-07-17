# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k ==1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            prev = kth.next
            curr = group_prev.next

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp