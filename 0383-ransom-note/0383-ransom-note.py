class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_counts = Counter(magazine)

        for char in ransomNote:
            if magazine_counts[char] <= 0:
                return False
            magazine_counts[char] -= 1
            
        return True