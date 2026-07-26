class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Sort citations in decending order
        citations.sort(reverse = True)

        h = 0

        #Iterate over papers ordered from highest citations to lowest
        for i, cite in enumerate(citations):
            # Check if there are at least (i + 1) papers at least (i + 1) citations
            if cite >= i + 1:
                h = i + 1

            else:
                break

        return h