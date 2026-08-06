class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths are different, they cannot be anagram
        if len(s) != len(t):
            return False

        count = {}

        # Count frequencies of characters in string s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Decrement counts using t
        for char in t:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1

        return True