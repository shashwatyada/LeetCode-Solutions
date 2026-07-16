# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to anchor the result
        dummy = ListNode(0)
        curr = dummy 

        # Traverse while both lists have elements to compare 
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1 
                list1 = list1.next
            else:
                curr.next = list2 
                list2 = list2.next

            curr = curr.next
        
        # Hook up any reamaining nodes from whichever list isn't empty yet
        curr.next = list1 if list1 else list2
        # Return the head of the merge list (skipping the dummy)
        return dummy.next