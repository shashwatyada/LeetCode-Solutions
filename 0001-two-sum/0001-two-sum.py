class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement was already encountered
            if complement in seen:
                return [seen[complement], i]

            #store the index of the current number
            seen[num] = i