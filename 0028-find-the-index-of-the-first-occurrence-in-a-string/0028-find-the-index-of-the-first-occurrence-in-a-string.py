class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len = len(haystack)
        n_len = len(needle)

        # If needle is longer than haystack, it can't be a substring
        if n_len > h_len:
            return -1 

        # Iterate through the haystack up to the last possible starting index
        for i in range(h_len - n_len +1):
            # Check if the substring slice matches the needle
            if haystack[i: i + n_len] == needle:
                return i
        return -1