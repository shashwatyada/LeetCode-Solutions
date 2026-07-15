class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengtha are different, they can not be isomorphic
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}
        for char_s, char_t in zip(s, t):
            # Check s -> t mapping consistency 
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t 
            
            # Check t -> s mapping consistency to prevent double mapping
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            
            else:
                map_t_to_s[char_t] = char_s
        return True
