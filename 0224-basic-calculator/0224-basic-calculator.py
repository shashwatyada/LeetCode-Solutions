class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        curr_num = 0
        sign = 1 # 1 represents positive, -1 represents negative

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in "+-":
                # Add the completed number to the running sum
                result += sign * curr_num
                curr_num = 0
                sign = 1 if char == '+' else -1
            elif char in '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset result and sign for the inside of the parenthesis
                result = 0
                sign = 1
            elif char == ')':
                # Add the completed inner number to the inner result
                result += sign * curr_num
                curr_num = 0
                # Multiply by sign before '(' and add to result before '('
                result *= stack.pop()  # pop sign
                result += stack.pop()  # pop saved result

        # Add any trailing number left at the end of the string
        return result + sign * curr_num