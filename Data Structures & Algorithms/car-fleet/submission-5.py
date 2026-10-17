class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        m = {}
        for i in range(len(position)):
            m[position[i]] = (target-position[i]) / speed[i]
        
        position.sort()

        fleets = 0
        prev = 0
        for i in range(len(position)-1, -1, -1):
            car = position[i]
            time = m[car]
            if time > prev:
                fleets += 1
                prev = time
        
        return fleets


