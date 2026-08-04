class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse Left to Right across top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # 2. Traverse Top to Bottom down right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3. Traverse Right to Left across bottom row (check boundary)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse Bottom to Top up left column (check boundary)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result    