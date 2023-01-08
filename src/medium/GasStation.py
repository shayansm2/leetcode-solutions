class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        if len(gas) == 1:
            return 0

        index = None
        sumSoFar = 0

        for i in range(0, len(gas)):
            value = gas[i] - cost[i]

            if index is not None:
                sumSoFar += value
                if sumSoFar < 0:
                    index = None
                    sumSoFar = 0
            
            if index is None and value > 0:
                index = i
                sumSoFar = value
        
        return index

