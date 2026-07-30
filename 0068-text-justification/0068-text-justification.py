class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur_line = []
        num_of_letters = 0

        for word in words:
            # Check if adding word exceeds maxWidth (accounting for 1 space between words)
            if num_of_letters + len(word) + len(cur_line) > maxWidth:
                # Format current line
                if len(cur_line) == 1:
                    # Single word line: left-justified
                    res.append(cur_line[0] + ' ' * (maxWidth - num_of_letters))
                else:
                    # Fully justified line
                    total_spaces = maxWidth - num_of_letters
                    slots = len(cur_line) - 1
                    space_per_slot = total_spaces // slots
                    extra_spaces = total_spaces % slots

                    for i in range(slots):
                        cur_line[i] += ' ' * space_per_slot + (' ' if i < extra_spaces else '')
                    
                    res.append(''.join(cur_line))
                
                # Reset for next line
                cur_line = []
                num_of_letters = 0

            cur_line.append(word)
            num_of_letters += len(word)

        # Last line: left-justified
        last_line = ' '.join(cur_line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res