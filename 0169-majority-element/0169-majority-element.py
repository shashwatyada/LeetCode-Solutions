class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            # If our candidates loses all votes, pick the current number as the new candidate
            if count == 0:
                candidate = num

            # Adjust the voting power 
            if num == candidate:
                count += 1

            else:
                count -= 1
        return candidate 