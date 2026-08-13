class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        if n < total_len:
            return []
            
        word_count = Counter(words)
        result = []
        
        # Run sliding window for each word_len starting offset
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    # Shrink window if word frequency exceeds target count
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # Valid concatenation found
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset window on encountering an invalid word
                    current_count.clear()
                    count = 0
                    left = right
                    
        return result