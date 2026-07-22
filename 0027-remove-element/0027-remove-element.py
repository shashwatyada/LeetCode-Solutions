class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Pointer 'k' keeps track of the index where the next valid elements goes
        k = 0 

        # Loop through the array 'i' as our scanner 
        for i in range(len(nums)):
            # If the current element is NOT the value we want to remove
            if nums[i] != val:
                # Assinging to it our valid position 'k'
                nums[k] = nums[i]
                # Move 'k' forward
                k +=1 
        
        # Return the count of valid element
        return k