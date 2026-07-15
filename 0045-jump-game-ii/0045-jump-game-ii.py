class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farther = 0

        for i in range(len(nums) - 1):
            farther = max(farther, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farther

                if current_end >= len(nums) - 1:
                    break

        return jumps