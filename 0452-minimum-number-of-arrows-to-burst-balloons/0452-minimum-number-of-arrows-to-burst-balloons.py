class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # Sort balloons by their end coordinate (x_end)
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        prev_end = points[0][1]
        
        for start, end in points[1:]:
            # If the balloon starts after the last arrow position, shoot a new arrow
            if start > prev_end:
                arrows += 1
                prev_end = end
                
        return arrows