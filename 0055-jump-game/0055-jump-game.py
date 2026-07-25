class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Set the initial goalpost to the last index
        goalpost = len(nums) -1

        # Move backward through the array starting from the second-to-last element
        for i in range(len(nums)-2, -1,-1):
            # If we can reach or the current goalpost from index i
            if i + nums[i] >= goalpost:
                # Move the goalpost closer to the start
                goalpost = i

        # If the goalpost reaches the very fist index, a path exist
        return goalpost == 0 