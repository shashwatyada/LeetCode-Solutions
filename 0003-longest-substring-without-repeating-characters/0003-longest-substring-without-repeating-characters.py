class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_chars = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            
            # If we've seen this char and it's in the current window, move 'left' past it
            if char in seen_chars and seen_chars[char] >= left:
                left = seen_chars[char] + 1
                
            # Record/update the most recent index of the character
            seen_chars[char] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)

        return max_length