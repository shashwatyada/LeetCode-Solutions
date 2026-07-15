class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array has 2 or fever elements, it's already valid
        if len(nums) <= 2:
            return len(nums)

        # Start tracking insertions from index 2
        insert_index = 2

        # Loop from index 2 to the end of the array 
        for i in range(2, len(nums)):
            # Check if the current number is different from the number 2 slots behind 
            if nums[i] != nums[insert_index - 2]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index
