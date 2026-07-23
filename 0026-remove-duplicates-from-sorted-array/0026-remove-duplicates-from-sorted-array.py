class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Starts at index 1 because the first element is always unique 
        insert_index = 1 

        # Loop through the array starting from index 1
        for i in range(1 , len(nums)):
            # If current nubmer is NOT equal to the previos number
            if nums[i] != nums[i-1]:
                # 1. Copy the unique number to the insert_index position
                nums[insert_index] = nums[i]
                # 2. Increment insert_index by 1
                insert_index += 1
                
        return insert_index         
