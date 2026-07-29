class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of Roman numeral symbols and their values in descending order
        value_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), 
            (1, "I")
        ]

        res = []
        for value, symbol in value_symbols:
            if num == 0:
                break
            
            # Count how many times value fits into num
            count, num = divmod(num, value)
            # Append the corresponding symbol 'count' times
            res.append(symbol * count)

        return "".join(res)