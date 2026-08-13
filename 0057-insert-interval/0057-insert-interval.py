class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        for i, interval in enumerate(intervals):
            # Case 1: Current interval ends before newInterval starts
            if interval[1] < newInterval[0]:
                res.append(interval)
            # Case 2: Current interval starts after newInterval ends
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                # Append the rest of intervals and return
                return res + intervals[i:]
            # Case 3: Overlap detected — merge bounds into newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        # Append merged newInterval if loop completes without triggering Case 2
        res.append(newInterval)
        return res