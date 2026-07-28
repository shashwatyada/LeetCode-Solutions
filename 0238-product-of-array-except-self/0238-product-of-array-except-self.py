class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # Step 1: Calculate prefix products (product of elements to the left)
        prefix = 1
        for i in range(n):
            answer[i] = prefix 
            prefix *= nums[i]

        # Step 2: Multiply by suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]         

        return answer