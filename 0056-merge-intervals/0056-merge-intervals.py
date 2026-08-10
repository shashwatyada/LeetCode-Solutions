class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort intervals by their start time
        intervals.sort(key = lambda x: x[0])

        merged = []

        for interval in intervals:
            # If merged is empty or there is no overlap, append the internet
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                # Overlap exist: Update the end time of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged