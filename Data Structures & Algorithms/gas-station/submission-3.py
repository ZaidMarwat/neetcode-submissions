class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        cursum = -1
        startStation = -1
        i = 0 
        while True:
            i = i % len(gas)
            if cursum < 0:
                cursum = 0
                startStation = i
            elif startStation == i:
                break
            
            cursum += gas[i] - cost[i]

            i += 1
        
        return startStation