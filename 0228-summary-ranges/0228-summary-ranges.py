class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # Extend range while consecutive numbers are found
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            # Format single element or range string
            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append("{}->{}".format(start, nums[i]))
            
            i += 1
            
        return ans