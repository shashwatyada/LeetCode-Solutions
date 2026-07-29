class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # If total gas is less than total cost, it's imposible to complete the loop
        if sum(gas) < sum(cost):
            return -1

        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            net_gas = gas[i] - cost[i]
            curr_tank += net_gas

            # If current tank drops below 0, reset start position to the next position
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index 