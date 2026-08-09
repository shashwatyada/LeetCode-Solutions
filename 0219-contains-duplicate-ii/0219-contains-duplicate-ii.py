class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i, num in enumerate(nums):
            # If element was seen before and distance <= k:
            if num in seen and i - seen[num] <= k:
                return True

            # Update the most recent index for the element
            seen[num] = i

        return False