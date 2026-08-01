class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # Step 1: Short the array to enables two-pointer traversal and easy duplication
        nums.sort()

        for i in range(len(nums) - 2):
            # Optimization: If the first element is > 0, three positive numbers can't sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the fixed first element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res