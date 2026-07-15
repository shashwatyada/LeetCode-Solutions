class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0:
            return 0 

        candies = [1] * n

        # left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # right to left pass 
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i], candies[i + 1] + 1)
                    
         # Sum up the optimal allocation matrix
        return sum(candies)