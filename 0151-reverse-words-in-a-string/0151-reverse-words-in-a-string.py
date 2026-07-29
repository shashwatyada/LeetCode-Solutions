class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s.split() automatically strips extra spaces and splits by whitespaces
        words = s.split()

        # Reverse the list of words and join them with a single space
        return " ".join(words[::-1])