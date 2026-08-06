class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        
        # If lengths don't match, a 1-to-1 mapping is impossible
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            # Check existing mapping consistency for character
            if c in char_to_word and char_to_word[c] != w:
                return False
            # Check existing mapping consistency for word
            if w in word_to_char and word_to_char[w] != c:
                return False
            
            char_to_word[c] = w
            word_to_char[w] = c
            
        return True