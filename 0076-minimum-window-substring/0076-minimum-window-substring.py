from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""

        # frequency map for charaters in t
        count_t = Counter(t)
        required = len(count_t)

        # Track counts in current window
        window = {}
        have = 0

        # Stores (length, left, right) of smallest valid window
        res = (-1, -1)
        res_len = float("inf")
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Check if current character satisfies target frequency in t
            if char in count_t and window[char] == count_t[char]:
                have += 1
                
            # Try to shrink window from left once all characters are matched
            while have == required:
                # Update smallest window result
                if (right - left + 1) < res_len:
                    res = (left, right)
                    res_len = right - left + 1
                    
                # Pop left character to shrink window
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""