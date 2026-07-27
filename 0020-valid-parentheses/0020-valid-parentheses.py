class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in mapping:
                # Pop top element if stack is non-empty, else use dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if matching open bracket matches the required one
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # If stack is empty, all brackets were validly matched
        return len(stack) == 0